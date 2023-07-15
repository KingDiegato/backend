from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from models.object import PyObjectId

class Admins(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    last_name: str
    email: str
    dni: int
    birthdate: str
    phone: int
    
    class Config:
       orm_mode = True
       allow_population_by_field_name = True
       json_encoders = {ObjectId: str}
       
class UpdateAdmins(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    dni: Optional[int] = None
    birthdate: Optional[str] = None
    phone: Optional[int] = None
    
    class Config:
       orm_mode = True
       allow_population_by_field_name = True
       json_encoders = {ObjectId: str}