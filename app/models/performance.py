from pydantic import BaseModel,Field

from datetime import datetime

class Performance(BaseModel):
    candidate_mail:str
    score: int
    sentiment_score:int
    jobrole: str
    analyzed_at: datetime = Field(default_factory=datetime.utcnow)