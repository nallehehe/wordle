from beanie import Document, Link
from pydantic import Field
from models import Word
from typing import List
from datetime import datetime


class Game(Document):
    word: Link[Word]
    attempts: int = Field(default=0, ge=0, le=6)
    completed: bool = False
    won: bool = False
    guesses: List[str] = []
    created_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "games"
