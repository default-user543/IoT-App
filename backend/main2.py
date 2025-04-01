from flask import Flask, jsonify, request
import re
import string
from firebase_admin import credentials, initialize_app, db
import bcrypt
from math import radians, sin, cos, sqrt, atan2

app = Flask(__name__)
cred=credentials.Certificate('key.json')
initialize_app(cred, {
    'databaseURL': 'https://iot-project-863b1-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
ref=db.reference('users')

def calculate_space(la1, lo1, la2, lo2): # To calculate the distance between user and the defined location, we use haversine formula:
    R=6371000
    phi1, phi2=radians(la1), radians(la2)
    delta_phi=radians(la2-la1)
    delta_lambda=radians(lo2-lo1)

    a=sin(delta_phi/2)**2 + cos(phi1) * cos(phi2) * sin(delta_lambda/2)**2
    c=2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

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
        'GPS': {
            'latitude': 0,
            'longitude': 0
        },
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

if __name__ == "__main__":
    app.run(debug=True)
