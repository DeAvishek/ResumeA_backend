from fastapi import APIRouter, HTTPException
from app.models.performance import Performance
from app.collections.performance_collection import performance_collection

router = APIRouter()

@router.post("/add/performance")
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