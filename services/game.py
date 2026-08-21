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

    if game.completed:
        raise HTTPException(status_code=400, detail="Game is already over")
    
    normalized_guess = guess.strip().lower()

    if normalized_guess in game.guesses:
        raise HTTPException(
            status_code=400, detail="You've already guessed that.")
    
    guess_attempt = guess.strip().lower() == game.word.name.strip().lower()

    game.guesses.append(guess.strip().lower())

    if guess_attempt:
        game.won = True
        game.completed = True
    else:
        game.attempts += 1
        if game.attempts >= 6:
            game.completed = True

    await game.save()
    return game
