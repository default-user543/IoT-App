import requests, json 

# Đây là một cái test example cho việc gửi yêu cầu có chứa session cookies.
BASE_URL="http://127.0.0.1:5000"

def login():
    payload= {
        "username": "Đức Võ Lay",
        "password": "111111@"
    }
    response=requests.post(f"{BASE_URL}/login", json=payload)
    return response.cookies 

def user_information(cookies):
    payload={
        "city": "New York",
        "fav_colour": "blue",
        "fav_pet": "dog",
        "country": "USA",
        "language": "English",
        "reset_password": "Hmuhmu"
    }
    response=requests.post(f"{BASE_URL}/user-information", json=payload, cookies=cookies)
    return cookies 

def run_test():
    cookies=login()
    cookies=user_information(cookies)

if __name__ == "__main__":
    print("Starting Flask API tests...")
    print("=" * 50)
    run_test()