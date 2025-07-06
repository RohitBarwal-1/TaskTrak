from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://tickettrak_dev:Development_123@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&authSource=TicketTrak&appName=mongosh+2.5.5"
client = AsyncIOMotorClient(MONGO_URI)
