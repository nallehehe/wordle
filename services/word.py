from models import Word
from fastapi import HTTPException
from datetime import datetime


async def insert_word(name: str):
    existing_word = await Word.find_one(Word.name == name)
    if existing_word:
        raise HTTPException(status_code=409, detail="Word already exists")
    if len(name) != 5:
        raise HTTPException(status_code=400, detail="Word must be 5 letters")
    if not name.isalpha():
        raise HTTPException(status_code=400, detail="Only letters are allowed")
    word = Word(name=name)
    await word.insert()
    return word


async def new_word():
    words = await Word.find_all().sort(Word.updated_at).to_list()
    if not words:
        raise HTTPException(status_code=404, detail="No words found")

    last_used_word = words[0]
    last_used_word.updated_at = datetime.utcnow()

    await last_used_word.save()

    return last_used_word
