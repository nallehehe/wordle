from models import Game
from fastapi import HTTPException
from services.word import new_word
from beanie import PydanticObjectId


async def new_game():
    word = await new_word()
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")

    game = Game(
        word=word,
    )

    await game.insert()

    return game


async def game_guess(game_id: PydanticObjectId, guess: str):
    game = await Game.get(game_id, fetch_links=True)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    print(guess)
    return game
