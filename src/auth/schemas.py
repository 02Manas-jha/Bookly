from pydantic import BaseModel, Field
from src.books.schemas import BookSchema
from src.reviews.schemas import ReviewModel
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

class UserBookModel(UserModel):
    books: List[BookSchema]
    reviews: List[ReviewModel] 

class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)

class EmailModel(BaseModel):
    addresses: List[str]

class PasswordResetRequestModel(BaseModel):
    email: str

class PasswordResetConfirmModel(BaseModel):
    new_password: str
    confirm_new_password: str