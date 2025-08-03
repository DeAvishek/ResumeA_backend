from fastapi import APIRouter,HTTPException
from models.admin import Adminuser
from my_collections.performance_collection import admin_user_collection

router2 = APIRouter()

@router2.post("/admin/create_account")
async def create_account(adminuser :Adminuser):
    try:
        exist_user = admin_user_collection.find_one({"email":adminuser.email})
        if exist_user:
            raise HTTPException(status_code=400,detail="User exists")
        new_user = admin_user_collection.insert_one(adminuser.dict())
        return {"message":"Account created","Username":adminuser.username}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
        
