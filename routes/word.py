from fastapi import APIRouter
from models import Word
from services import insert_word

router = APIRouter()


@router.post("/word")
async def create_word(body: Word):
    return await insert_word(body.name)

@router.get("/words")
async def get_words():
    words = await Word.find_all().to_list()
    return words