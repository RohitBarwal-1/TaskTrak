import logging
from fastapi import APIRouter, Request
from database.models.users_model import Users

router = APIRouter("/auth")
logger = logging.getLogger(__name__)

@router.post("/signup")
def signup(request: Request, user:Users):
    data = await request.json()
    logger.info("received request %s", data)

    

    