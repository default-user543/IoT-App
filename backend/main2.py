from flask import Flask, jsonify, request
import re
import string
from firebase_admin import credentials, initialize_app, db
import bcrypt
from shapely.geometry import Point, Polygon

app = Flask(__name__)
cred=credentials.Certificate('key.json')
initialize_app(cred, {
    'databaseURL': 'https://app-du-lich-4d8a4-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

def check_location_algorithm(latitude, longitude, poly): # This is the function to check whether the user is in the location or not.
    point = Point(latitude, longitude)
    polygon = Polygon([(p['lat'], p['lng']) for p in poly])
    return polygon.contains(point)

def check_name(username): # This is the function to check the username data.
    if not (6 <= len(username) <= 20):
        return "The username must be between 6 and 20 characters."
    if not re.match(r"^[a-zA-Z0-9ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểẾỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰửữự ]+$", username):
        return "The username cannot contain special characters."
    return None

def check_password(password, confirm_password): # This is the function to check the password data.
    if password != confirm_password:
        return "Password and confirm password do not match."
    if len(password) <= 6:
        return "Password must be longer than 6 characters."
    if not any(char in string.punctuation for char in password):
        return "Password must contain at least one special character."
    return None

def find_user_by_username(username):
    users_ref = db.reference('users')
    all_users = users_ref.get() or {}
    for key, user_data in all_users.items():
        if user_data.get("username") == username:
            return key, user_data
    return None, None

@app.route('/sign-up', methods=['POST'])
def signup():
    ref=db.reference('users')
    user = request.get_json()
    username = user.get('username')
    password = user.get('password')
    confirm_password = user.get('confirm_password')

    if not username or not password or not confirm_password:
        return jsonify({'message': 'Please provide all the information!'})
    all_users=ref.get() or {}
        
    message=check_name(username)
    if message:
        return jsonify({'message': message})
    message=check_password(password, confirm_password)
    if message:
        return jsonify({'message': message})
    for key, user_data in all_users.items():
        if user_data['username'] == username:
            return jsonify({'message': 'Username is already existed!'})
    
    salt=bcrypt.gensalt()
    hashed_password=bcrypt.hashpw(password.encode('utf-8'), salt)
    hashed_password=hashed_password.decode('utf-8')

    user_data={
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

    ref.push(user_data)
    return jsonify({'message': 'Successfully!'}), 200

@app.route('/check-location', methods=["POST"])
def check_location():
    data=request.get_json()
    latitude=data['latitude']
    longitude=data['longitude']

    if not latitude or not longitude:
        return jsonify({"message": "Cannot get the GPS of the user!"})
    
    ref = db.reference('zones')
    zones = ref.get()

    for zone_id, zone_data in zones.items():
        polygon = zone_data['polygon']
        if check_location_algorithm(latitude, longitude, polygon):
            return jsonify({
                "message": "Sucessfully!",
                "name": zone_data['name']
            })
    
    return jsonify({
        "message": "No zone found!"
    })

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Please provide all required fields!", "a": 6}), 400
    message=check_name(username)
    if message:
        return jsonify({'message': message}), 400
    message=check_password(password, password)
    if message:
        return jsonify({'message': message}), 400
    
    user_key, user_data = find_user_by_username(username)
    if not user_data:
        return jsonify({"message": "Account does not exist!", "a": 8}), 404

    stored_password = user_data.get("password")
    if not bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        return jsonify({"message": "Incorrect password!", "a": 8}), 401

    return jsonify({"message": "Login successful!", "a": 0}), 200


if __name__ == "__main__":
    app.run(debug=True)
