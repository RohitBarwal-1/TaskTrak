import bcrypt
import jwt
import logging
import os
import uuid
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi import HTTPException, status
from jwt import ExpiredSignatureError, InvalidTokenError
from models.users_model import Users

logger = logging.getLogger(__name__)
load_dotenv() 
SECRET_KEY = os.getenv("JWT_SECRET", "super-secret-key")
ALGORITHM = "HS256"
TOKEN_EXPIRY_DAYS = 7

async def signup_service(body,user_db):
    try:
        existing_user  = await user_db.find({"email": body.email})
        if existing_user:
            logger.error("User already registered")
            return {"error": "User already exists"}
        
        new_user = Users(
            user_id= get_user_id(body.email),
            first_name= body.first_name,
            last_name= body.last_name,
            email= body.email,
            is_active= body.is_active,
            password= get_hashed_password(body.password)
        )

        logger.info("Registering new user %s", new_user)

        await user_db.insert(new_user)
        logger.info("New user signup successfully 😊")
        return {"message": "User created successfully"}
    except Exception as e:
         logger.error("Signup for new user failed 😞 :: %s",e)
         
async def login_service(body, user_db):
    logger.info("Trying to authenticate")
    try:
        user = await user_db.find({"email":body.email})
        if not user:
            logger.error("User with email %s does not exist", body.email)
            return {"message":"Invalid email or password, try again"}
    except Exception as e:
        logger.error("Error while fetching user data")
        return {"message":"Invalid email or password, try again"}
    try:
        if not verify_password(body.password, user["password"]):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        token = create_access_token(
                                    data={"email": user["email"], "user_id": user["user_id"]},
                                    expires_delta=timedelta(days=TOKEN_EXPIRY_DAYS)
                                )
    except Exception as e:
        return False
    return {"access_token" : token, "token_type" : "bearer"}


def get_user_id(email:str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, email)) 

    
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

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Can be removed if not required
async def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")