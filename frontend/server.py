from flask import Flask, request, jsonify

app = Flask(__name__)

# Dữ liệu lưu tạm
latest_data = {}

@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    data = request.get_json()
    print("Received data:", data)

    # Lưu dữ liệu lại để frontend lấy
    latest_data = data
    return jsonify({"status": "success"}), 200

@app.route('/latest', methods=['GET'])
def get_latest():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
