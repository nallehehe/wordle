from fastapi import APIRouter, HTTPException
from models import Word
from services import insert_word, random_word
from beanie import PydanticObjectId

router = APIRouter()


@router.post("/word")
async def create_word(body: Word):
    return await insert_word(body.name)


@router.get("/words")
async def get_words():
    words = await Word.find_all().to_list()
    if not words:
        raise HTTPException(status_code=404, detail="Words not found")
    return words


@router.get("/word/random")
async def get_random_word():
    return await random_word()


@router.get("/word/{word_id}")
async def get_word(word_id: PydanticObjectId):
    word = await Word.get(word_id)
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")
    return word
