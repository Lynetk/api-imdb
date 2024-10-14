from movies import top_movies
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# List of movies
movies = top_movies

# Pydantic model for a movie
class Movie(BaseModel):
    title: str
    year: int
    imdb_rating: float
    cast: list

# Get all movies
@app.get("/movies/", response_model=list[Movie])
async def get_movies():
    return movies

# Get a single movie by title
@app.get("/movies/{title}", response_model=Movie)
async def get_movie(title):
    for movie in movies:
        if movie["title"] == title:
            return movie
    return {"error": "Movie not found"}

