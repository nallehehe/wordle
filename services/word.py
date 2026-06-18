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
    # check if a word has been picked today
    todays_word = await Word.find(Word.last_used_date == date.today()).first_or_none()
    if todays_word:
        return todays_word

    # if no word has been picked, find one that hasn't been used
    unused_word = await Word.find(Word.last_used_date == None).first_or_none()
    if unused_word:
        unused_word.last_used_date = date.today()
        await unused_word.save()
        return unused_word

    # if all words have been used find the word with the oldest last_used_date and use that
    find_word = await Word.find_all().sort(Word.last_used_date).first_or_none()
    find_word.last_used_date = date.today()
    await find_word.save()
    return find_word
