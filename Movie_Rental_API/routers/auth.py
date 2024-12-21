import json
from passlib.context import CryptContext
from fastapi import FastAPI, HTTPException

from Movie_Rental_API.main import USER_FILE
from Movie_Rental_API.models.schemas import User
from Movie_Rental_API.utils.auth_utils import create_jwt_token

USER_FILE = "users.json"
pwd_context = CryptContext(schemes='sha256_crypt')
app = FastAPI()


def read_users():
  try:
    with open(USER_FILE) as file:
      return json.load(file)
  except json.JSONDecodeError:
    return {}

@app.post("/auth/register")
def register_user(user: User):
    users = read_users()
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already registered")

    hashed_password = pwd_context.hash(user.password)
    users[user.username] = {"username": user.username, "password": hashed_password}

    with open(USER_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=2)
    return "Success"


def authenticate_user(user: User) -> bool:
    users = read_users()
    current_user = users.get(user.username)
    if not current_user:
        return False
    return True

@app.post("/auth/login")
def login_user(user: User):
    if not authenticate_user(user):
        raise HTTPException(status_code=401, detail="Invalid authentication")
    auth_token = create_jwt_token({"sub": user.username})
    return {"auth_token": auth_token}
