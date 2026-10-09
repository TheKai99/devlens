from fastapi import FastAPI
from src.github.routers import git_routes



app = FastAPI(title="github analyzer")

app.include_router(git_routes)





