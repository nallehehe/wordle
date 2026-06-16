from fastapi import FastAPI
from database import connect
from routes.word import router as word_router
from routes.game import router as game_router

app = FastAPI()

app.include_router(word_router)
app.include_router(game_router)


@app.on_event("startup")
async def startup():
    await connect()
