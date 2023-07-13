from motor.motor_asyncio import AsyncIOMotorClient as AsyncIOMotorClient
from models import Client

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
    return await collection.find_one({"_id": id})

async def create_user(user):
    new_user = await collection.insert_one(user)
    created_user = await collection.find_one({"_id": new_user.inserted_id})
    return created_user
    
async def update(id: int, client):
    await collection.update_one({"_id": id}, {"$set": client})
    document = await collection.find_one({"_id": id})
    return document

async def delete(id: int):
    await collection.delete_one({"_id": id})
    return True