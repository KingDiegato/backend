from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
        
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

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