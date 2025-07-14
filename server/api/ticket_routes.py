import logging
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from models.ticket_model import tickets
from controller.ticket_controller import create_ticket_controller,get_tickets_controller,update_tickets_controller,delete_tickets_controller

router = APIRouter(prefix="/ticket", tags=["ticket"])
logger = logging.getLogger(__name__)

@router.get("/")
async def get_tickets(request: Request):
    data = request.json()
    user_id = data.user_id
    logger.info("Received request to get all tickets for user %s",user_id)
    result = await get_tickets_controller(data,request.app.database,user_id)
    return result
    
@router.post("/")
async def create_ticket(request:Request, tickets:tickets):
    data = await request.json()
    # user_id = data.user_id
    logger.info("Creating ticket for user %s",data)
    result = await create_ticket_controller(data,request.app.database,data)
    return JSONResponse(content={"result":result})

@router.patch("/")
async def update_ticket(request:Request, tickets:tickets):
    data = await request.json()
    user_id = data.user_id
    logger.info("Received request to get all tickets for user %s",user_id)
    result = await update_tickets_controller(data,request.app.database,user_id)
    return result

@router.delete("/")
async def delete_ticket(request:Request, tickets:tickets):
    data = await request.json()
    user_id = data.user_id
    logger.info("Received request to get all tickets for user %s",user_id)
    result = await delete_tickets_controller(data,request.app.database,user_id)
    return result