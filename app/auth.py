from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "CHANGE_ME"
ALGORITHM = "HS256"

def create_access_token():
    expire = datetime.utcnow() + timedelta(hours=1)
    payload = {"sub": "admin", "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
