from models import Word
from fastapi import HTTPException


async def insert_word(name: str):
    existing_word = await Word.find_one(Word.name == name)
    if existing_word:
        raise HTTPException(status_code=409, detail="Word already exists")
    if len(name) != 5:
        raise HTTPException(status_code=400, detail="Word must be 5 letters")
    word = Word(name=name)
    await word.insert()
    return word
