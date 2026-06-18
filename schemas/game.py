from pydantic import BaseModel
from pydantic import Field


class GuessRequest(BaseModel):
    guess: str = Field(min_length=5, max_length=5)
