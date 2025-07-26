import firebase_admin
from firebase_admin import credentials, auth

# Only initialize once
if not firebase_admin._apps:
    cred = credentials.Certificate("backend/firebase_admin_config.json")
    firebase_admin.initialize_app(cred)

def verify_id_token(id_token: str):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token  # includes uid, email, etc.
    except Exception as e:
        return None
