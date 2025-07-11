from .auth_routes import router as auth_routes #when main / start point file is in same directory then need to add . at start
from .ticket_routes import router as ticket_routes
from contextlib import asynccontextmanager
from database.constants import TTConstants
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient


app = FastAPI()

# Event handler for application startup
# @app.on_event("startup")
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient(TTConstants.MONGO_URI)
    app.database = app.mongodb_client[TTConstants.Database]
    yield
    app.mongodb_client.close()
    
# Create a FastAPI application instance
app = FastAPI(lifespan=lifespan)

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("shutdown")
# async def shutdown_db_client():
#     app.mongodb_client.close()

app.include_router(auth_routes)
app.include_router(ticket_routes)

# @app.exception_handler(TicketException)
# async def tickets_exception_handler(request: Request, exc: TicketException):
#     logger.error(traceback.format_exc())
#     return JSONResponse(
#         status_code=500,
#         content={"message": "There was an issue in the persistence layer"},
#     ) 
