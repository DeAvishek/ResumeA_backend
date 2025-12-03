from pydantic import BaseModel,Field
from datetime import datetime
class Performance(BaseModel):
    candidate_mail:str
    score: int
    analyzed_at: datetime = Field(default_factory=datetime.utcnow)