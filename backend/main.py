# Please follow the structure following the comment to make the code clean!
from flask import Flask, jsonify, request
import requests, json
import re, string
import dns.resolver
from firebase_admin import credentials, auth, initialize_app
# This is the area for config information:
app=Flask(__name__)
authe="https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyAFVY0tJ2mDjkmKZJ6MeO1JdeNBXDlpmAg"
# The format of auth is: "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=<API_FIREBASE_AUTHENTICATION_KEYS>"
# Team Backend nếu muốn chạy code thì có thể copy key API của Firebase Console vào phần <>.

def check_email(domain):
    try: 
        mx_check=dns.resolver.resolve(domain, 'MX')
        return len(mx_check) > 0
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        return False
@app.route('/sign-up', methods=['POST'])
def signup():
    user=request.get_json() # the frontend team will send a json file which contain username and password to the backend team.
    email=user.get('email')
    password=user.get('password')

    # This block of code is used to check whether the input is invalid or not!
    if not user or not user.get('email') or not user.get('password') or not user.get('confirm_password'):
        return jsonify({'message': 'Please provide all the information!'})
    if user.get('password') != user.get('confirm_password'):
        return jsonify({'message': 'Password and confirm password are not the same!'})
    if len(user.get('password')) <= 6:
        return jsonify({'message': 'Password must be longer than 6 characters!'})
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', user.get('email')): # Check the patern of an email.
        return jsonify({'message': 'Your email is in invalid form!'})
    if not any(char in string.punctuation for char in user.get('password')):
        return jsonify({'message': 'The password has to be have at least 1 special character!'})
    domain=email.split('@')[1]
    if not check_email(domain):
        return jsonify({'message': "Your domain isn't existed"})
    user={
        'email': email,
        'password': password
    }
    user=requests.post(authe, json=user)
    return jsonify({'message': 'Sucessfully!'})

if __name__=="__main__":
    app.run(debug=True) 
