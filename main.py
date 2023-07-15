from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.admin import admin
from routes.client import client
import os

frontend = os.getenv("FRONTEND_URL")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin)
app.include_router(client)
