from beanie import Document
from pydantic import Field
from datetime import date


class Word(Document):
    name: str = Field(min_length=5, max_length=5)
    last_used_date: date | None = None

    class Settings:
        name = "words"
