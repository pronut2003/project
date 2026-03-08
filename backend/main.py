from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.db import Base, engine
from models.models import *
from controllers.studentcontroller import router as StudentsRouter
import os

ENV = os.getenv("ENV")

app = FastAPI()

#Enable Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#Create Tables
Base.metadata.create_all(bind=engine)

#Register all routes
app.include_router(StudentsRouter)

@app.get("/")
def home():
    return "Started...."