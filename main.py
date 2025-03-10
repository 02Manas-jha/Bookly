from fastapi import FastAPI, Header
from typing import Optional

from pydantic import BaseModel

app = FastAPI()

class UserSchema(BaseModel):
    username: str
    email: str

users = []

@app.post("/create_user")
async def create_user(user_data:UserSchema):
    new_user = {
        "username": user_data.username,
        "email": user_data.email
    }

    users.append(new_user)
    return {"message":"User created successfully", "user":new_user}

@app.get('/')
async def read_root():
    return {"message": "Hello world!"}

@app.get('/greet')
async def greet_name(name:Optional[str] = "User",age:int = 0) -> dict:
    return {"message": f"Hello {name}!", "age":age}

# inside main.py
@app.get('/get_headers')
async def get_all_request_headers(
    user_agent: Optional[str] = Header(None),
    accept_encoding: Optional[str] = Header(None),
    referer: Optional[str] = Header(None),
    connection: Optional[str] = Header(None),
    accept_language: Optional[str] = Header(None),
    host: Optional[str] = Header(None),
):
    request_headers = {}
    request_headers["User-Agent"] = user_agent
    request_headers["Accept-Encoding"] = accept_encoding
    request_headers["Referer"] = referer
    request_headers["Accept-Language"] = accept_language
    request_headers["Connection"] = connection
    request_headers["Host"] = host

    return request_headers
