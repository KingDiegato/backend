from motor.motor_asyncio import AsyncIOMotorClient as AsyncIOMotorClient
from models import Admins, UpdateAdmins
from bson import ObjectId

app = AsyncIOMotorClient("mongodb://localhost:27017")

database = app.new_database
collection = database.admins

async def get_all_admins():
    admins = []
    helper = collection.find({})
    async for document in helper:
        admins.append(Admins(**document))
    return admins

async def get_single_admin(id):
    return await collection.find_one({"_id": ObjectId(id)})

async def get_admin_by_email(email):
    return await collection.find_one({"email": email})

async def create_admin(admin):
    new_admin = await collection.insert_one(admin)
    created_admin = await collection.find_one({"_id": new_admin.inserted_id})
    return created_admin
    
async def update_single_admin(id: str, data):
    admin = { key:value for key, value in data.dict().items() if value is not None }
    print(admin)
    print("before")
    await collection.update_one({"_id": ObjectId(id)}, {"$set": admin})
    print("after")
    document = await collection.find_one({"_id": ObjectId(id)})
    response = Admins(**document)
    return response

async def delete_single_admin(id: str):
    return collection.delete_one({"_id": ObjectId(id)})

async def delete_single_admin_email(email: str):
    collection.delete_one({"email": email})
    return True