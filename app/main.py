from fastapi import FastAPI
from routes.performance import router
from routes.adminusers import router2
from fastapi.middleware.cors import CORSMiddleware
from routes.parsing import router3
from dotenv import load_dotenv
import os
load_dotenv()
server = FastAPI()
env = os.getenv("ENV")
if env =="dev":
    frontendurl = os.getenv("FRONTEND_URL_DEV")
else:
    frontendurl = os.getenv("FRONTEND_URL_PROD")
    

origins = [
    frontendurl
]

server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],  # Allow POST, GET, PUT, DELETE, OPTIONS
    allow_headers=["*"],  # Allow all headers
)

server.include_router(router,prefix="/api")
server.include_router(router2,prefix="/user")
server.include_router(router3,prefix="/analyze")
