import requests, json 

response=requests.post("http://127.0.0.1:5000/check_location", json={"lat": 11.108313675344915, "lng": 106.6142607874415})
print(response.json())