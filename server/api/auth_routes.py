import logging
from controller.auth_controller import signup_controller
from db_service.auth_db_services import get_user_collection
from fastapi import APIRouter, Request, Depends
from models.users_model import Users

router = APIRouter(prefix="/auth", tags=["auth"])
logger = logging.getLogger(__name__)

@router.post("/signup")
async def signup(request: Request, User_data: Users, user_db= Depends(get_user_collection) ):
    logger.info("Received new signup request :)")
    return await signup_controller(body=User_data, user_db=user_db)

@router.post("/login")
async def login(request:Request, user):
    # user_id, user_password = await get_user(user.username)
    # if not user_id:
    #     raise Exception('Invalid username or password')
    # try:
    #     verify_password(user.user_password,user_password)
    # except: 
    #      raise Exception('Invalid username or password')
    return True
     


