from database.constants import TTConstants
from fastapi import Depends
from database.mongo_client import get_mongo_db
from pymongo.database import Database
from pymongo.collection import Collection

def get_ticket_collection(db: Database = Depends(get_mongo_db) ):
    collection = db[TTConstants.TICKETS]
    return TicketDbService(collection)


class TicketDbService(): #need to create a baserepo class and inhert it here
    def __init__(self, collection: Collection):
        self.collection = collection
    

    def insert(self, database, data):
        try:
            result = database[TTConstants.TICKETS].insert_one(data.dict())
        except Exception as e:
            raise e
        return result
    
    # def insert(self, Obj):
    #     return self.collection.insert_one(Obj.dict())