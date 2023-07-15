from fastapi import APIRouter, HTTPException
from database.admin import (
    get_all_admins,
    create_admin,
    get_admin_by_email,
    get_single_admin,
    delete_single_admin_email,
    update_single_admin
)
from models.admin import Admins, UpdateAdmins

admin = APIRouter()

@admin.get("/ping")
def welcome():
    return {"ping": "pong"}

@admin.get("/api/admins")
async def get_admins():
    admins = await get_all_admins()
    return admins

@admin.get("/api/admins/by_id/id", response_model=Admins)
async def get_admin_by_id(admin_id):
    admin = await get_single_admin(admin_id)
    if admin:
        response_model = Admins(**admin)
        return response_model
    raise HTTPException(detail="Admin not found", status_code=404)

@admin.get("/api/admins/by_email/email", response_model=Admins)
async def get_single_admin_email(email: str):
    admin = await get_admin_by_email(email)
    if admin:
        response_model = Admins(**admin)
        return response_model
    raise HTTPException(detail="Admin not found", status_code=404)

@admin.post("/api/admins/new", response_model=Admins)
async def new(admin: Admins):
    admin_found = await get_admin_by_email(admin.email)
    if admin_found:
        raise HTTPException(detail="email already exists", status_code=409)

    new_admin = await create_admin(admin.dict())
    if new_admin:   
        response_model = Admins(**new_admin)
        return response_model
    
    raise HTTPException(detail="SOMETHING WENT WRONG", status_code=400)

@admin.delete("/api/admins/by_email/email")
async def delete_admin_email(email: str):
    admin = await get_admin_by_email(email)
    if admin:
        await delete_single_admin_email(email)
        return "Admin has been deteled successfully"
    raise HTTPException(detail="Admin not found", status_code=404)

@admin.delete("/api/admins/by_id/id")
async def delete_admin(id:str):
    try:
        admin = await get_single_admin(id)
        response = Admins(**admin)
        if admin:
            await delete_admin(response.id)
            return "Admin has been deteled successfully"
    except Exception as e:
        raise HTTPException(detail=e, status_code=404)

@admin.put("/api/admins/by_id/id", response_model=Admins)
async def update_admin(id:str, admin: UpdateAdmins):
    response = await update_single_admin(id, admin)
    if response:
        return response
    raise HTTPException(detail="Admin not found", status_code=404)
