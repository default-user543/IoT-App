import requests

# Bạn có thể import biến từ file config riêng nếu muốn
CLIENT_ID = "LowoizKOivUnKygMuXcXSBUe6XBtaB3P"
CLIENT_SECRET = "h8S4Kf2JG9WXoyC8cxVV4dpujv69AhmC2ljAcPqErF3bxOQfYAlHoR8CCWWW3juK"
REFRESH_TOKEN = "<YOUR_REFRESH_TOKEN>"

def refresh_access_token():
    url = "https://api2.arduino.cc/iot/v1/clients/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": "https://api2.arduino.cc/iot"
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        token = response.json().get("access_token")
        return token
    else:
        print("❌ Lỗi khi refresh token:", response.status_code, response.text)
        return None
