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
        
    for key, user_data in all_users.items():
        if user_data['username'] == username:
            return jsonify({'message': 'Username is already existed!'})
    
    message=check_name(username)
    if message:
        return jsonify({'message': message})
    message=check_password(password, confirm_password)
    if message:
        return jsonify({'message': message})
    
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

if __name__ == "__main__":
    app.run(debug=True)
