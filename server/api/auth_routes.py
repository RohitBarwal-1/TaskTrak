import logging
from controller.auth_controller import signup_controller, login_controller
from db_service.auth_db_services import get_user_collection
from fastapi import APIRouter, Request, Depends
from models.users_model import Users, UserLogin

router = APIRouter(prefix="/auth", tags=["auth"])
logger = logging.getLogger(__name__)

@router.post("/signup")
async def signup(request: Request, User_data: Users, user_db= Depends(get_user_collection) ):
    logger.info("Received new signup request :)")
    return await signup_controller(body=User_data, user_db=user_db)

@router.post("/login")
async def login(request:Request, User_data: UserLogin, user_db= Depends(get_user_collection)):
    logger.info("Received request to authenticate")
    return await login_controller(User_data, user_db)
     


