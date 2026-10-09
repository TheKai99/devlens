from fastapi import APIRouter
from src.github import services
from src.github.dtos import Githubprofile



git_routes = APIRouter(prefix="/github")


@git_routes.get("/{username}" , response_model=Githubprofile)
async def get_github_profile(username:str):
    return await services.github_service(username)