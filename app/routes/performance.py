from fastapi import APIRouter, HTTPException
from models.performance import Performance
from my_collections.performance_collection import performance_collection
from bson import ObjectId

router = APIRouter()

async def add_performance(performance: Performance):
    try:
        result = performance_collection.insert_one(performance.dict())
        return {"message": "Performance added", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get/performance")
async def get_performance():
    try:
        performances = performance_collection.find()
        print(performances)
        performance_list = []
        for it in performances:
            it["_id"] = str(it["_id"])
            performance_list.append(it)
        return performance_list
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))
    

@router.get("/get/{id}/performance")
async def get_performance(id:str):
    try:
        result = performance_collection.find_one({"_id":ObjectId(id)})
        if not result:
            raise HTTPException(status_code=403,detail="not data found")
        result["_id"] = str(result["_id"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))