import logging
from db_service.tickets_db_services import TicketDbService

logger = logging.getLogger(__name__)

async def get_ticket_service(database,data):
    pass

async def create_ticket_service(ticket, database, data, db):
    try:
        db.insert(database=database, data=ticket)
        return True
    except Exception as e:
        raise e
async def update_ticket_service(database,data):
    pass
async def delete_ticket_service(database,data):
    pass