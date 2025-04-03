import requests, json 

response=requests.post("http://127.0.0.1:5000/check-location", json={"latitude": 11.109248409517255, "longitude": 106.6176708740449})
print(response.json())