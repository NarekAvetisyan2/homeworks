import json
from fastapi import FastAPI
from Movie_Rental_API.models.schemas import Movie

movie_file="movies.json"

app = FastAPI()

@app.get("/movies")
def get_movies():
    try:
        with open(movie_file) as file:
            new_movies = json.load(file)
            return new_movies
    except FileNotFoundError:
        return []

@app.post("/movies")
def create_movies(movie: Movie):
    try:
        with open(movie_file) as file:
            new_movies = json.load(file)
    except FileNotFoundError:
        return {"Error": "File not found"}
    except json.JSONDecodeError as e:
        return e
    new_movies.append(movie.dict())

    try:
        with  open(movie_file, "w") as file:
            json.dump(new_movies, file, indent=2)
    except Exception as e:
        return e