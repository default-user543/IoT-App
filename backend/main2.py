from flask import Flask, jsonify, request
import re
import string

app = Flask(__name__)

@app.route('/sign-up', methods=['POST'])
def signup():
    user = request.get_json()
    username = user.get('username')
    password = user.get('password')
    confirm_password = user.get('confirm_password')

    if not username or not password or not confirm_password:
        return jsonify({'message': 'Please provide all the required information!'})

    if password != confirm_password:
        return jsonify({'message': 'Password and confirm password do not match!'})

    if len(password) <= 6:
        return jsonify({'message': 'Password must be longer than 6 characters!'})

    if not any(char in string.punctuation for char in password):
        return jsonify({'message': 'Password must contain at least one special character!'})

    if not (6 <= len(username) <= 20):
        return jsonify({'message': 'The username must be above 6 and below 20 characters!'})
    
    if not re.match(r"^[a-zA-Z0-9ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểẾỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰửữự ]+$", username):
        return jsonify({'message': 'The username cannot contain special characters!'})

    return jsonify({'message': 'Successfully!'})

if __name__ == "__main__":
    app.run(debug=True)
