import logging
from service.auth_service import signup_service

logger = logging.getLogger(__name__)

async def signup_controller(body,user_db):
    logger.info("Entering the signup controller")
    await signup_service(body,user_db)