import os
from ai21 import AI21Client
from fastapi import APIRouter, HTTPException
from ai21.models.chat import ChatMessage
from dotenv import load_dotenv
load_dotenv()
router = APIRouter()
system_prompt = "you are an job recomendation engine based on skill"

@router.post('/ai/jobrecomendation')
async def getRecomenadtion(data: dict):
    try:
        skill = data.get("AllSkills")
        print(skill)
        print("hii")
        if not skill:
            raise HTTPException(status_code=400, detail="AllSkills is required")
        user_prompt = f"""Using the user's skills {skill}, suggest the 
                        top 3 suitable jobs and why this job with in 20 words
                        like: job|why"""
        API_key = os.getenv('AI21_LAB')
        if not API_key:
            raise HTTPException(status_code=500, detail="API key not found")
        client = AI21Client(
            api_key=API_key
        )
        message = [
            ChatMessage(content=system_prompt, role="system"),
            ChatMessage(content=user_prompt, role="user"),
        ]
        chat_completions = client.chat.completions.create(
            messages=message,
            model="jamba-instruct",
        )
        content = chat_completions.choices[0].message.content
        print(content)
        return {"recommendations": content, "status": 200}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    