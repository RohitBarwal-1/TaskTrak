from database.constants import TTConstants
from database.mongo_client import get_mongo_db
from fastapi import Depends
from pymongo.collection import Collection
from pymongo.database import Database

def get_user_collection(db:Database = Depends(get_mongo_db)):
    collection = db[TTConstants.USERS]
    return AuthDbService(collection)


class AuthDbService():
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, obj):
        return self.collection.insert_one(obj.dict())