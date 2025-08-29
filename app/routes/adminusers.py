from fastapi import APIRouter,HTTPException
from models.admin import Adminuser
from my_collections.performance_collection import admin_user_collection
from models.login import Loginuser

router2 = APIRouter()

@router2.post("/admin/create_account")
def create_account(adminuser :Adminuser):
    try:
        exist_user = admin_user_collection.find_one({"email":adminuser.email})
        if exist_user:
            raise HTTPException(status_code=400,detail="User exists")
        adminuser = adminuser.dict()
        new_user = admin_user_collection.insert_one(adminuser)
        return {"message":"Account created","status":200}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
        
#another for login
@router2.post("/admin/log_in")
def log_in(loginuser:Loginuser):
    try:
        exist_user = admin_user_collection.find_one({"email":loginuser.email})
        if exist_user:
            getpassword = exist_user["password"]
            if getpassword == loginuser.password:
                return  {"message":"Logged in successfully","status":200}
            raise HTTPException(status_code=400,detail="Invalid credentials")
        raise HTTPException(status_code=400,detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
            