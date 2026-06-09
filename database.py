from dotenv import load_dotenv, find_dotenv
import os
from pymongo import AsyncMongoClient
from models import Word
from beanie import init_beanie


load_dotenv(find_dotenv())

connection_string = os.getenv("MONGO_URI")


async def connect():
    client = AsyncMongoClient(os.getenv("MONGO_URI"))
    await init_beanie(
        database=client.wordle,
        document_models=[Word]
    )
