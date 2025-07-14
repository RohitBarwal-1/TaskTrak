import logging
from fastapi import APIRouter, Request
from models.actions_model import actions

router = APIRouter("/ticket")
logger = logging.getLogger(__name__)

@router.get("/")
def get_actions(request: Request):
    data = request.json()
    user_id = data.user_id
    return True
    
@router.post("/")
def create_ticket(request:Request, actions:actions):
    data =  request.json()
    return True

@router.patch("/")
def update_ticket(request:Request, actions:actions):
    data = request.json()
    return True

@router.delete("/")
def delete_ticket(request:Request, actions:actions):
    data = request.json()
    return True