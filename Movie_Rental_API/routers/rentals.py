import json
from fastapi import FastAPI, Depends
from jose import JWTError
from Movie_Rental_API.models.schemas import Rental
from Movie_Rental_API.utils.auth_utils import verify_jwt_token
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="j_token")

RENTAL_FILE="rental.json"
app = FastAPI()

def read_rents():
    try:
        with open(RENTAL_FILE) as file:
            new_rents = json.load(file)
            return new_rents
    except FileNotFoundError:
        return []

@app.post("/rentals")
def create_rent(rental: Rental, j_token: str = Depends(oauth2_scheme)):
    try:
        if not verify_jwt_token(j_token):
            raise JWTError("Token not authorized")
        rentals = read_rents()
        rentals[rental.title] = {"username":rental.user}
    except Exception as e:
        return {e}

    with open(RENTAL_FILE, "w") as file:
        json.dump(rentals, file, indent=2)
    return "rent success"

@app.get("/rentals")
def history_rents(j_token: str = Depends(oauth2_scheme)):
    try:

        if not verify_jwt_token(j_token):
            raise JWTError("Token not authorized")
        rentals = read_rents()
        for rental in rentals:
            if rental["username"]  == verify_jwt_token(j_token):
                return rental["username"]
    except JWTError:
        return {"Error": "Authorization error"}
    except json.JSONDecodeError:
        return {"Error": "JSON Error"}
