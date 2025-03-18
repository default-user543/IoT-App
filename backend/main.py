# Please follow the structure following the comment to make the code clean!
from flask import Flask, jsonify, request
import requests, json
import re 

# This is the area for config information:
app=Flask(__name__)
auth="https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyAFVY0tJ2mDjkmKZJ6MeO1JdeNBXDlpmAg"

@app.route('/sign-up', methods=['POST'])
def signup():
    user=request.get_json() # the frontend team will send a json file which contain username and password to the backend team.

    # This block of code is used to check whether the input is invalid or not!
    if not user or not user.get('email') or not user.get('password') or not user.get('confirm_password'):
        return jsonify({'message': 'Please provide all the information!'})
    if user.get('password') != user.get('confirm_password'):
        return jsonify({'message': 'Password and confirm password are not the same!'})
    if len(user.get('password')) <= 6:
        return jsonify({'message': 'Password must be longer than 6 characters!'})
    if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', user.get('email')):
        return jsonify({'message': 'Your email is in invalid form!'})
    
    email=user.get('email')
    password=user.get('password')
    user={
        'email': email,
        'password': password,
    }
    user=requests.post(auth, json=user)
    return jsonify({'message': 'Sucessfully!'})
if __name__=="__main__":
    app.run(debug=True) 