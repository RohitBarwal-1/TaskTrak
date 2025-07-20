import uuid
import bcrypt
import logging
from models.users_model import Users

logger = logging.getLogger(__name__)

# TODO: CHeck if email already exist and give error
async def signup_service(body,user_db):
    try:
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
        logger.info("New user signup successfully :)")
    except Exception as e:
         logger.error("Signup for new user failed :( :: %s",e)
         

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