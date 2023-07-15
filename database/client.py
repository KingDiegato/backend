from motor.motor_asyncio import AsyncIOMotorClient as AsyncIOMotorClient
from models.clients import Client
from bson import ObjectId

app = AsyncIOMotorClient("mongodb://localhost:27017")

database = app.new_database
collection = database.clients

async def get_all_clients():
    clients = []
    helper = await collection.find({})
    async for document in helper:
        clients.append(Client(**document))
    return clients

async def get_single_client(id):
    return await collection.find_one({"_id": ObjectId(id)})

async def get_client_by_email(email):
    return await collection.find_one({"email": email})

async def create_user(user):
    new_user = await collection.insert_one(user)
    created_user = await collection.find_one({"_id": new_user.inserted_id})
    return created_user
    
async def update(id: int, data):
    client = { key:value for key, value in data.dict().items() if value is not None }
    await collection.update_one({"_id": id}, {"$set": client})
    document = await collection.find_one({"_id": id})
    response = Client(**document)
    return response

async def delete_single_client(id: int):
    await collection.delete_one({"_id": id})
    return True

async def delete_single_client_by_email(email: str):
    await collection.delete_one({"email": email})
    return True