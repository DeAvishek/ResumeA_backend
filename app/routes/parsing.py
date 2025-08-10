from fastapi import APIRouter,UploadFile,Form,HTTPException
import os
import shutil
router3 = APIRouter()
@router3.post("/upload")
def parsing_resume_jobdesc(jobdesc:str=Form(...),file:UploadFile = None):
    try:
        if file:
            upload_dir = "backend/app/uploads"
            os.makedirs(upload_dir,exist_ok=True)
            filpath = os.path.join(upload_dir,file.filename)
            with open(f"uploads/{file.filename}","wb") as buffer:
                shutil.copyfileobj(file.file,buffer)
            return {"message":"Upload completed","status":200}
        #process this
        #and return somethimg
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
        
        
    
    
    
    
    
    
    
    
    
    