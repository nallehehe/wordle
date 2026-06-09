from fastapi import FastAPI
from database import connect, Word
app = FastAPI()


@app.on_event("startup")
async def startup():
    await connect()


@app.post("/word")
async def create_word(body: Word):
    word = Word(name=body.name)
    await word.insert()
    return word
