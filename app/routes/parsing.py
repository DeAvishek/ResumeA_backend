from fastapi import APIRouter,UploadFile,Form
import os
import shutil
router3 = APIRouter()
@router3.post("/upload")
def parsing_resume_jobdesc(jobdesc:str=Form(...),file:UploadFile = None):
    if file:
        upload_dir = "backend/app/uploads"
        os.makedirs(upload_dir,exist_ok=True)
        filpath = os.path.join(upload_dir,file.filename)
        with open(f"uploads/{file.filename}","wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
            
        #process this
        #and return somethimg
    
    
    
    
    
    
    
    
    
    