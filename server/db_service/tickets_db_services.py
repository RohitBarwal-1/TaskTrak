from database.constants import TTConstants


class TicketDbService:
    def __init__(self) -> None:
        pass
    
    def insert(self, database, data):
        # obj = data.dict()
        try:
            result = database[TTConstants.TICKETS].insert_one(data)
        except Exception as e:
            raise e
        return result