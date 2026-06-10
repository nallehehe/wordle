from models import Word
from fastapi import HTTPException


async def insert_word(name: str):
    if len(name) != 5:
        raise HTTPException(status_code=404, detail="Word must be 5 letters")
    word = Word(name=name)
    await word.insert()
    return word
