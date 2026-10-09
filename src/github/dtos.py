from pydantic import BaseModel , field_serializer
from datetime import datetime


class Githubprofile(BaseModel):

    username:str
    name:str|None
    avatar:str
    profile_url:str
    bio:str|None
    followers:int
    following:int
    repos:int
    joined_on:datetime

    @field_serializer('joined_on')
    def format_date(self , value:datetime):
        return value.strftime("%B %d , %Y").lower()