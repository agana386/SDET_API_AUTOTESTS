from pydantic import BaseModel


class Post(BaseModel):
    id: int | None = None
    title: str
    body: str
    userId: int