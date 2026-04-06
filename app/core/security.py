from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "vishwas_key_12345"
ALGORITHM = "HS256"

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=8)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


