import os
from datetime import timedelta, datetime
import jwt
from dotenv import load_dotenv
from jose import JWTError


load_dotenv()

EXPIRE_MINUTE = int(os.getenv("EXPIRE_MINUTE", 30))
SECRET_KEYS = os.getenv("SECRET_KEYS")
ALGORITHM = os.getenv("ALGORITHM")


def create_jwt_token(user: dict):
    try:
        expires_time = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTE)
        date = user.copy()
        date['exp'] = expires_time
        j_token = jwt.encode(date, SECRET_KEYS, algorithm=ALGORITHM)
        return j_token
    except JWTError:
        raise TypeError("Token not created")

def verify_jwt_token(j_token):
    try:
        user = jwt.decode(j_token, SECRET_KEYS, ALGORITHM)
        return user
    except JWTError:
        raise TypeError("Verification error")
    except jwt.ExpiredSignatureError:
        raise ValueError("Token was expired")
