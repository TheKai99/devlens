import httpx
from src.github.dtos import Githubprofile

async def github_service(username:str):
    async with httpx.AsyncClient() as client:
    
            profiledata = await client.get(f"https://api.github.com/users/{username}")
    
            #repodata = await client.get("https://api.github.com/users/TheKai99/repos")
    
            profiledata = profiledata.json()
            #repodata = repodata.json()

            profiledata_using = Githubprofile(
                username=profiledata['login'],
                name=profiledata['name'],
                avatar = profiledata['avatar_url'],
                profile_url= profiledata['html_url'],
                bio= profiledata['bio'],
                followers= profiledata['followers'],
                following= profiledata['following'],
                repos= profiledata['public_repos'],
                joined_on= profiledata['created_at'],
            )
    
            return profiledata_using