from pymongo import MongoClient
from .constants import TTConstants

client = MongoClient(TTConstants.MONGO_URI)
db = client[TTConstants.Database]

def get_mongo_db():
    return db