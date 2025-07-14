import logging
from db_service.tickets_db_services import TicketDbService

logger = logging.getLogger(__name__)

async def get_ticket_service(database,data):
    pass

async def create_ticket_service(database,data):
    TicketDbService().insert(database=database, data=data)

async def update_ticket_service(database,data):
    pass
async def delete_ticket_service(database,data):
    pass