from fastapi import APIRouter, HTTPException
from services import new_game
from beanie import PydanticObjectId
from models import Game


router = APIRouter()


@router.post("/game")
async def create_word():
    return await new_game()


@router.get("/game/{game_id}")
async def get_game(game_id: PydanticObjectId):
    game = await Game.get(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game
