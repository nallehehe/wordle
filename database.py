import os
from dotenv import load_dotenv, find_dotenv
from pymongo import AsyncMongoClient
from models import Word, Game
from beanie import init_beanie


load_dotenv(find_dotenv())

connection_string = os.getenv("MONGO_URI")


async def connect():
    client = AsyncMongoClient(os.getenv("MONGO_URI"))
    await init_beanie(
        database=client.wordle,
        document_models=[Word, Game]
    )
