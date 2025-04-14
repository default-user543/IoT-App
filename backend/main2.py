from flask import Flask, jsonify, request, session, redirect, url_for
import re
import string
from firebase_admin import credentials, initialize_app, db
import bcrypt
from shapely.geometry import Point, Polygon
from flask_session import Session
from datetime import timedelta
from flask_session import Session 
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = "no_one_knows_this_secret_key"
cred = credentials.Certificate('key.json')
initialize_app(cred, {
    'databaseURL': 'https://app-du-lich-4d8a4-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
app.permanent_session_lifetime = timedelta(days=365)

def check_location_algorithm(latitude, longitude, poly):
    point = Point(latitude, longitude)
    polygon = Polygon([(p['lat'], p['lng']) for p in poly])
    return polygon.contains(point)

def check_name(username):
    if not (6 <= len(username) <= 20):
        return "The username must be between 6 and 20 characters.", 1
    if not re.match(r"^[a-zA-Z0-9ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểẾỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰửữự ]+$", username):
        return "The username cannot contain special characters.", 2
    return None, 0

def check_password(password, confirm_password=None):
    if confirm_password and password != confirm_password:
        return "Password and confirm password do not match.", 3
    if len(password) <= 6:
        return "Password must be longer than 6 characters.", 4
    if not any(char in string.punctuation for char in password):
        return "Password must contain at least one special character.", 5
    return None, 0

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def find_user_by_username(username):
    users_ref = db.reference('users')
    all_users = users_ref.get() or {}
    for key, user_data in all_users.items():
        if user_data.get("username") == username:
            return key, user_data
    return None, None

@app.route('/sign-up', methods=['POST'])
def signup():
    user = request.get_json()
    username = user.get('username')
    password = user.get('password')
    confirm_password = user.get('confirm_password')
    ref=db.reference('users')

    if not username or not password or not confirm_password:
        return jsonify({'message': 'Please provide all the information!', 'a': 6}), 400

    all_users = ref.get() or {}
    for key, user_data in all_users.items():
        if user_data['username'] == username:
            return jsonify({'message': 'Username is already existed!', 'a': 7}), 400

    message, code = check_name(username)
    if code != 0:
        return jsonify({'message': message, 'a': code}), 400

    message, code = check_password(password, confirm_password)
    if code != 0:
        return jsonify({'message': message, 'a': code}), 400

    ref = db.reference(f'users/{username}')
    hashed_password = hash_password(password)
    user_data = {
        'username': username,
        'password': hashed_password,
        'forget_password': {
            'city': '',
            'fav_color': '',
            'fav_pet': '',
            'country': '',
            'language': '',
        }
    }
    session['username']=username 
    session.permanent = True
    ref.update(user_data)
    return jsonify({'message': 'Successfully!', 'a': 0}), 200

@app.route('/check-location', methods=["POST"])
def check_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    timestamp = data.get('timestamp')

    if "username" not in session:
        return jsonify({'message': 'Please login or sign up first!'}), 400
    username = session['username']
    if not latitude or not longitude:
        return jsonify({"message": "Cannot get the GPS of the user!", "a": 6}), 400

    ref = db.reference('zones')
    zones = ref.get()

    for zone_id, zone_data in zones.items():
        polygon = zone_data['polygon']
        if check_location_algorithm(latitude, longitude, polygon):
            return jsonify({
                "message": "Found zone successfully!",
                "name": zone_data['name'],
                "a": 0
            }), 200
    ref = db.reference(f"users/{username}/History_GPS")
    ref.push({
        "lat": latitude,
        "lng": longitude,
        "timestamp": timestamp
    })
    return jsonify({
        "message": "No zone found!",
        "a": 8
    }), 404

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Please provide all required fields!", "a": 6}), 400

    user_key, user_data = find_user_by_username(username)
    if not user_data:
        return jsonify({"message": "Account does not exist!", "a": 8}), 404

    stored_password = user_data.get("password")
    if not bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        return jsonify({"message": "Incorrect password!", "a": 8}), 401

    session['username'] = username
    session.permanent = True
    return jsonify({"message": "Login successful!", "a": 0}), 200

@app.route('/user-information', methods=['POST'])
def user_information():
    data = request.get_json()
    if 'username' not in session:
        return jsonify({"message": "Please login or sign up!"})
    username=session['username']
    required_fields = ["city", "fav_colour", "fav_pet", "country", "language"]

    if not all(field in data and data[field] for field in required_fields):
        return jsonify({"message": "Missing required information!", "a": 6}), 400

    message, code = check_name(username)
    if code != 0:
        return jsonify({'message': message, 'a': code}), 400

    users_ref = db.reference(f'users')
    user_key, user_data = find_user_by_username(username)

    if not user_data:
        return jsonify({"message": "User not found!", "a": 8}), 404

    users_ref.child(user_key).update({
        "forget_password": {
            "city": data["city"],
            "fav_colour": data["fav_colour"],
            "fav_pet": data["fav_pet"],
            "country": data["country"],
            "language": data["language"]
        }
    })

    return jsonify({"message": "Information updated successfully!", "a": 0}), 200

@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    required_fields = ["city", "fav_colour", "fav_pet", "country", "language", "reset_password"]
    if "username" not in session:
        return jsonify({"message": "Please login or sign up!"})
    username = session['username']

    if not all(field in data and data[field] for field in required_fields):
        return jsonify({"message": "Missing required information!", "a": 6}), 400
    
    user_key, user_data = find_user_by_username(username)
    users_ref = db.reference('users')

    if not user_data:
        return jsonify({"message": "User not found!", "a": 8}), 404

    forgot_info = user_data.get("forget_password", {})
    for field in ["city", "fav_colour", "fav_pet", "country", "language"]:
        if forgot_info.get(field) != data.get(field):
            return jsonify({"message": "Information does not match our records!", "a": 8}), 401

    new_password = data["reset_password"]
    message, code = check_password(new_password)
    if code != 0:
        return jsonify({'message': message, 'a': code}), 400

    new_hashed = hash_password(new_password)
    users_ref.child(user_key).update({"password": new_hashed})

    return jsonify({"message": "Password reset successful!", "a": 0}), 200

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logout successful!", "a": 0}), 200

if __name__ == "__main__":
    app.run(debug=True)