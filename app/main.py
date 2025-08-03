from fastapi import FastAPI
from routes.performance import router
from routes.adminusers import router2
server = FastAPI()
server.include_router(router,prefix="/api")
server.include_router(router2,prefix="/user")
