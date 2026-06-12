from beanie import Document
from pydantic import Field
from datetime import datetime


class Word(Document):
    name: str = Field(min_length=5, max_length=5)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "words"
