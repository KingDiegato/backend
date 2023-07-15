from motor.motor_asyncio import AsyncIOMotorClient as AsyncIOMotorClient
from models.employee import Employee
from bson import ObjectId

app = AsyncIOMotorClient("mongodb://localhost:27017")

database = app.new_database
collection = database.employees

async def get_all_employees():
    employees = []
    helper = await collection.find({})
    async for document in helper:
        employees.append(Employee(**document))
    
    return employees

async def get_single_employee(id):
    return await collection.find_one({"_id": id})

async def create_employee(employee):
    new_employee = await collection.insert_one(employee)
    created_employee = await collection.find_one({"_id": new_employee.inserted_id})
    return created_employee
    
async def update(id: int, employee):
    await collection.update_one({"_id": id}, {"$set": employee})
    document = await collection.find_one({"_id": id})
    return document

async def delete(id: int):
    await collection.delete_one({"_id": id})
    return True