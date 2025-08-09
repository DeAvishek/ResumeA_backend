from fastapi import FastAPI
from routes.performance import router
from routes.adminusers import router2
from fastapi.middleware.cors import CORSMiddleware
from routes.parsing import router3
server = FastAPI()
origins = [
    "http://localhost:3000",  # Next.js dev
    # "https://yourfrontend.com"  # Production
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
