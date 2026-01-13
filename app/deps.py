from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from .auth import SECRET_KEY, ALGORITHM

security = HTTPBearer()

def get_current_user(token=Depends(security)):
    try:
        jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return True
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
