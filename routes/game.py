from fastapi import APIRouter, HTTPException
from models import Game
from services import new_game

router = APIRouter()


@router.post("/game")
async def create_word():
    return await new_game()
