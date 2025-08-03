from pydantic import BaseModel,Field
from datetime import datetime
class Adminuser(BaseModel):
    username:str
    email:str
    password:str
    createdAt:datetime = Field(default_factory=datetime.now)