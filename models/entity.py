# models/entity.py
from pydantic import BaseModel


class Post(BaseModel):
    id: int | None = None
    title: str
    body: str
    userId: int


class PostPartial(BaseModel):
    """Модель для PATCH — все поля опциональные"""
    id: int | None = None
    title: str | None = None
    body: str | None = None
    userId: int | None = None