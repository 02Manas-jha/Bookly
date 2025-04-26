from pydantic import BaseModel, Field
from src.books.schemas import BookSchema
from datetime import datetime
from typing import List
import uuid

class UserCreateModel(BaseModel):
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    username: str = Field(max_length=8)
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)

class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    first_name: str
    last_name: str
    is_verified: bool
    email: str
    password_hash: str = Field(exclude=True)
    created_at: datetime
    updated_at: datetime
    books: List[BookSchema] 

class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)