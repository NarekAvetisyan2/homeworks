
import jwt
from dotenv import load_dotenv

from datetime import timedelta, timezone, datetime



USERS_FILE = {
    "username": "Bob",
    "password": 123456
  }



SECRET_KEY="secret_key"
ALGORITHM="HS256"
EXPIRE_MINUTE=30

load_dotenv()

def create_jwt_token(user :dict):
    expires = datetime.utcnow() + timedelta(seconds=EXPIRE_MINUTE)

    data = user.copy()

    data["exp"] = expires
    token = jwt.encode(data, SECRET_KEY, ALGORITHM)
    return token

def jwt_verify(token):
    username = jwt.decode(token, SECRET_KEY, ALGORITHM)
    return username



c = create_jwt_token(USERS_FILE)
print(c)
# token = create_jwt_token(USERS_FILE)
# print(jwt_verify(token))
# print(j)