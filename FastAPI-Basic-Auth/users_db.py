import json
from passlib.context import CryptContext

pwd_context = CryptContext(schemes="sha256_crypt")

def _initialize_user_file(users: dict):
    try:
        with open("users.json", "w") as file:
            json.dump(users, file, indent=2)
    except json.JSONDecodeError:
        return {"File error": "In file JSON's type error"}

def _read_user_file() -> dict:
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def register_user(username: str, password: str):
    db = _read_user_file()
    if username in db:
        return False
    db[username] = {"username": username, "password": hash_password(password)}
    _initialize_user_file(db)
    return True

def authenticate_user(username: str, password: str) -> bool:
    db = _read_user_file()
    user = db.get(username)
    if not user:
        return False
    return verify_password(password, user["password"])

