import json
from fastapi import FastAPI
from Movie_Rental_API.models.schemas import Movie

MOVIE_FILE="movies.json"

app = FastAPI()

@app.get("/movies")
def get_movies():
    try:
        with open(MOVIE_FILE, "r", encoding="utf-8") as file:
            new_movies = json.load(file)
            return new_movies
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return {"Error": "Error decoding JSON"}


@app.post("/movies")
def create_movies(movie: Movie):
    try:
        with open(MOVIE_FILE, "r", encoding="utf-8") as file:
            new_movies = json.load(file)
    except FileNotFoundError:
        return {"Error": "File not found"}
    except json.JSONDecodeError:
        return {"Error": "Decoding JSON"}

    new_movies.append(movie.dict())

    try:
        with  open(MOVIE_FILE, "w", encoding="utf-8") as file:
            json.dump(new_movies, file, indent=2)
    except Exception as e:
        return {"Error": f"{e}"}