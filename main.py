from fastapi import FastAPI
from database import connect
from routes import router as word_router

app = FastAPI()

app.include_router(word_router)


@app.on_event("startup")
async def startup():
    await connect()
