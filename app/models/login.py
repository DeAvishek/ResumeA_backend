from pydantic import BaseModel

class Loginuser(BaseModel):
    email:str
    password:str