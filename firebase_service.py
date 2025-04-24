import requests
from firebase_config import firebase_config

BASE_URL = firebase_config["databaseURL"]

def push_user(user_dict):
    url = f"{BASE_URL}/users.json"
    response = requests.post(url, json=user_dict)
    return response.json()
