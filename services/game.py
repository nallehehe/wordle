from models import Game
from fastapi import HTTPException
from services.word import new_word


async def new_game():
    word = await new_word()

    game = Game(
        word=word,
    )

    await game.insert()

    return game
