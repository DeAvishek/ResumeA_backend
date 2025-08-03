from fastapi import FastAPI
from routes.performance import router
server = FastAPI()
server.include_router(router,prefix="/api")
