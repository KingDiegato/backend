from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from models.object import PyObjectId

class Client(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    last_name: str
    email: str
    credits: int
    phone: str
    
    class Config:
       orm_mode = True
       allow_population_by_field_name = True
       json_encoders = {ObjectId: str}