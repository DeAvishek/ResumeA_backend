from fastapi import APIRouter,UploadFile,Form,HTTPException
from analyze import analyzer
import fitz
# import pymupdf
router3 = APIRouter()
@router3.post("/upload")
async def parsing_resume_jobdesc(jobdesc:str=Form(...),file:UploadFile = None):
    try:
        if file:
            pdf_bytes = await file.read()
            doc = fitz.open(stream=pdf_bytes,filetype ="pdf" )
            text =""
            for page in doc:
                text += page.get_text()
            doc.close()
            return analyzer(jobdesc,text)
        #process this
        #and return somethimg
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail=str(e))
    
        
        

    
    
    
    
    
    
    
    
    