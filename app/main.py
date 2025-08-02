from fastapi import FastAPI,APIRouter
from app.routes.add_performance import router
server = FastAPI()
server.include_router(router,prefix="/api")
