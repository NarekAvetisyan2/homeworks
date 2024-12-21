import os
import uvicorn
from dotenv import load_dotenv
from passlib.context import CryptContext
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes='sha256_crypt')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="j_token")
PORT = int(os.getenv("PORT"))
MOVIE_FILE = "movies.json"
USER_FILE = "users.json"
RENTAL_FILE = "rentals.json"

load_dotenv()
app = FastAPI()



if __name__ == "__main__":
    uvicorn.run("main:app", port= PORT , reload=True)