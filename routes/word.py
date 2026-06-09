from fastapi import APIRouter
from models import Word

router = APIRouter()


@router.post("/word")
async def create_word(body: Word):
    word = Word(name=body.name)
    await word.insert()
    return word
