from movies import top_movies
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Prometheus
Instrumentator().instrument(app).expose(app)

# List of movies
movies = top_movies

# Get all movies
@app.get("/movies/")
async def get_movies():
    return movies

# Get a single movie by title
@app.get("/movies/{title}")
async def get_movie(title):
    for movie in movies:
        if title.lower() in movie["title"].lower():
            return movie
    return {"error": "Movie not found"}

# Health check
@app.get("/health")
async def healtcheck():
    return {"message": "ok"}
