from fastapi import APIRouter


from database.client import (
    get_all_clients, 
    get_single_client,
    get_client_by_email
)

client = APIRouter()
