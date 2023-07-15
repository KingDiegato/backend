from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from models.object import PyObjectId

class Employee(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    last_name: str
    email: str
    dni: int
    birthdate: str
    phone: int
    game: str
    
    class Config:
       orm_mode = True
       allow_population_by_field_name = True
       json_encoders = {ObjectId: str}