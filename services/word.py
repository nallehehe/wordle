from models import Word
from fastapi import HTTPException
from datetime import date


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
    words = await Word.find_all().to_list()
    if not words:
        raise HTTPException(status_code=404, detail="No words found")

    used_word = min(words, key=lambda word: word.last_used_date or date.min)

    used_word.last_used_date = date.today()

    await used_word.save()

    return used_word
