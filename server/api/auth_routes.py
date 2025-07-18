import logging
import uuid
import bcrypt
from controller.auth_controller import signup_controller
from db_service.auth_db_services import get_user_collection
from fastapi import APIRouter, Request, Depends
from models.users_model import Users

router = APIRouter(prefix="/auth", tags=["auth"])
logger = logging.getLogger(__name__)

@router.post("/signup")
async def signup(request: Request, body: Users = Depends(get_user_collection) ):
    data = await request.json()
    logger.info("received request %s", data)
    return await signup_controller(body=body)

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
     

def get_user_id():
    return str(uuid.uuid5()) 

    
def get_hashed_password(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode('utf-8')
    
def verify_password(plain_password, hashed_password):
        # Encode the plain password and stored hashed password to bytes
        plain_password_bytes = plain_password.encode('utf-8')
        hashed_password_bytes = hashed_password.encode('utf-8')

        # Compare the plain password with the hashed password
        return bcrypt.checkpw(plain_password_bytes, hashed_password_bytes)
