from database.constants import TTConstants
from database.mongo_client import get_mongo_db
from fastapi import Depends
from pymongo.collection import Collection
from pymongo.database import Database
import logging
logger = logging.getLogger(__name__)

def get_user_collection(db:Database = Depends(get_mongo_db)):
    collection = db[TTConstants.USERS]
    return AuthDbService(collection)


class AuthDbService():
    def __init__(self, collection: Collection):
        self.collection = collection

    async def insert(self, obj):
        return self.collection.insert_one(obj.dict())
    
    async def find(self, obj):
        # If obj is a Pydantic model, convert to dict
        if hasattr(obj, "dict") and callable(obj.dict):
            query = obj.dict()
        else:
            query = obj

        logger.info("Searching with query: %s", query)
        return self.collection.find_one(query)