from beanie import Document
from pydantic import Field
from datetime import datetime


class Word(Document):   
    name: str = Field(min_length=5, max_length=5)
    last_used_date: datetime | None = None

    class Settings:
        name = "words"
