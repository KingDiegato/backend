from motor.motor_asyncio import AsyncIOMotorClient as AsyncIOMotorClient
from models import Admins
from bson import ObjectId

app = AsyncIOMotorClient("mongodb://localhost:27017")

database = app.new_database
collection = database.admins

async def get_all_admins():
    """
    Retrieves all the admins from the collection.

    :return: A list of Admins objects representing the admins in the collection.
    """
    admins = []
    helper = collection.find({})
    async for document in helper:
        admins.append(Admins(**document))
    return admins

async def get_single_admin(id):
    """
    Retrieves a single admin from the collection based on the given ID.

    Parameters:
        id (str): The ID of the admin to retrieve.

    Returns:
        dict: The admin document from the collection, or None if not found.
    """
    return await collection.find_one({"_id": ObjectId(id)})

async def get_admin_by_email(email):
    """
    Get the admin user with the given email.

    Args:
        email (str): The email of the admin user.

    Returns:
        dict: The admin user document, or None if not found.
    """
    return await collection.find_one({"email": email})

async def create_admin(admin):
    """
    Creates a new admin in the database.

    Args:
        admin (dict): A dictionary containing the details of the admin.

    Returns:
        dict: A dictionary representing the newly created admin.
    """
    new_admin = await collection.insert_one(admin)
    created_admin = await collection.find_one({"_id": new_admin.inserted_id})
    return created_admin
    
async def update_single_admin(id: str, data):
    """
    Updates a single admin in the database.

    Args:
        id (str): The ID of the admin to be updated.
        data: The data containing the updated admin information.

    Returns:
        Admins: The updated admin object.

    Note:
        - The `data` parameter should be a dictionary-like object that contains the updated admin information.
        - Only non-null values in the `data` dictionary will be updated in the admin object.
        - The admin object will be updated in the "collection" collection of the database.

    Example:
        >>> admin_data = {
        ...     "name": "John Doe",
        ...     "email": "johndoe@example.com",
        ...     "role": "admin"
        ... }
        >>> updated_admin = await update_single_admin("1234567890", admin_data)
        >>> print(updated_admin)
        {'_id': '1234567890', 'name': 'John Doe', 'email': 'johndoe@example.com', 'role': 'admin'}
    """
    admin = { key:value for key, value in data.dict().items() if value is not None }
    print(admin)
    print("before")
    await collection.update_one({"_id": ObjectId(id)}, {"$set": admin})
    print("after")
    document = await collection.find_one({"_id": ObjectId(id)})
    response = Admins(**document)
    return response

async def delete_single_admin(id: str):
    """
    Delete a single admin by their ID.

    :param id: The ID of the admin to delete.
    :type id: str
    :return: The result of the deletion operation.
    :rtype: pymongo.results.DeleteResult
    """
    return collection.delete_one({"_id": ObjectId(id)})

async def delete_single_admin_email(email: str):
    """
    Deletes a single admin email from the collection.

    :param email: The email of the admin to be deleted.
    :type email: str
    :return: True if the admin email was successfully deleted, False otherwise.
    :rtype: bool
    """
    collection.delete_one({"email": email})
    return True