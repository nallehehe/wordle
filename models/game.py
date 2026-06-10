from beanie import Document, Link
from pydantic import Field
from models import Word
from typing import List


class Game(Document):
    word: Link[Word]
    attempts: int = Field(default=0, ge=0, le=6)
    completed: bool = False
    won: bool = False
    guesses: List[str] = []

    class Settings:
        name = "games"
