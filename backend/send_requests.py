import requests, json 

response=requests.post("http://127.0.0.1:5000/login", json={
    "username": "Lay Võ Đức",
    "password": "1111111@"
})


print(response.json())