import os
import json
import uvicorn
from dotenv import load_dotenv
from jose import JWTError
from models.schemas import User, Rental
from passlib.context import CryptContext
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from utils.auth_utils import create_jwt_token, verify_jwt_token

pwd_context = CryptContext(schemes='sha256_crypt')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="j_token")
PORT = int(os.getenv("PORT"))
movie_file = "movies.json"
user_file = "users.json"
rental_file = "rentals.json"

load_dotenv()
app = FastAPI()



if __name__ == "__main__":
    uvicorn.run("main:app", port= PORT , reload=True)