from models import Word
from fastapi import HTTPException
import random
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


async def random_word():
    word = await Word.find_all().to_list()
    if not word:
        raise HTTPException(status_code=404, detail="No words found")

    random_found_word = random.choice(word)

    random_found_word.updated_at = datetime.utcnow()

    await random_found_word.save()

    return random_found_word
