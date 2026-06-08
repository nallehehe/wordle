from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
load_dotenv(find_dotenv())

connection_string = os.getenv("MONGO_URI")

client = MongoClient(connection_string)