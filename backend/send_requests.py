import requests
import json 

res = requests.post("http://127.0.0.1:5000/sign-up", json={
    "username": "Lay Võ Đức",
    "password": "11111111@",
    "confirm_password": "11111111@"
})

res = res.json()
print(res.get('message'))
