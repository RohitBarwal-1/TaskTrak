import logging
from service.ticket_service import (get_ticket_service,create_ticket_service,update_ticket_service,delete_ticket_service)
logger = logging.getLogger(__name__)

async def get_tickets_controller(data,database,user_id):
    logger.info("Entering to save ticket for the user %s",user_id)
    await get_ticket_service(database,data)

async def create_ticket_controller(ticket,database, data, db):
    # logger.info("Entering to save ticket for the user %s",user_id)
    logger.info("Entering to save ticket for the user")
    await create_ticket_service(ticket, database, data, db)
    
async def update_tickets_controller(data,database,user_id):
    logger.info("Entering to save ticket for the user %s",user_id)
    await update_ticket_service(database,data)

async def delete_tickets_controller(data,database,user_id):
    logger.info("Entering to save ticket for the user %s",user_id)
    await delete_ticket_service(database,data)