from models import Game
from fastapi import HTTPException
from services.word import new_word


async def new_game():
    word = await new_word()
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")

    game = Game(
        word=word,
    )

    await game.insert()

    return game
