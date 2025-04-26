from sqlmodel import SQLModel, Field, Column, Relationship
import sqlalchemy.dialects.postgresql as pg
from src.books import models
from typing import List
from datetime import date, datetime
import uuid

class User(SQLModel, table=True):
    __tablename__ = "user_accounts"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            unique=True,
            nullable=False,
            default=uuid.uuid4,
            info={"description":"Unique identifier for the user account"},
        )
    )

    username: str
    first_name: str
    last_name: str
    role: str = Field(
        sa_column=Column(
            pg.VARCHAR, 
            nullable=False, 
            server_default="user"
        )
    )
    is_verified: bool = False
    email: str
    password_hash: str = Field(exclude=True)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    books: List["models.BookSchema"] = Relationship(back_populates="user", sa_relationship_kwargs={'lazy':'selectin'})

    def __repr__(self) -> str:
        return f"<User {self.username}"