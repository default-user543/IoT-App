from firebase_admin import credentials, initialize_app, db

cred=credentials.Certificate('key.json')
initialize_app(cred, {
    'databaseURL': 'https://app-du-lich-4d8a4-default-rtdb.asia-southeast1.firebasedatabase.app/'
})