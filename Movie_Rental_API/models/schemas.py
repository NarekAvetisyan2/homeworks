from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=6)
    email: EmailStr

class Movie(BaseModel):
    title: str = Field(..., min_length=1)
    genre: str = Field(..., min_length=1)
    rating: float

class Rental(BaseModel):
    user: User
    movie: Movie
    rental_duration: float


