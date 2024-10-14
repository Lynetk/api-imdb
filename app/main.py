from movies import top_movies
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Prometheus
Instrumentator().instrument(app).expose(app)

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

# Health check'
@app.get("/health")
async def healtcheck():
    return {"message": "ok"}