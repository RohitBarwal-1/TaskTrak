import logging
from service.auth_service import signup_service,login_service

logger = logging.getLogger(__name__)

async def signup_controller(body, user_db):
    logger.info("Entering the signup controller")
    return await signup_service(body, user_db)

async def login_controller(body, user_db):
    logger.info("Someone is trying to login ⚠️⚠️")
    return await login_service(body, user_db)