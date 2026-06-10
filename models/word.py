from beanie import Document
from pydantic import Field


class Word(Document):
    name: str = Field(min_length=5, max_length=5)
