from pydantic import BaseModel, Field
from datetime import datetime

class Request(BaseModel):
    id: int = Field(None)
    event_id : int = Field(...)
    requester_id : str = Field(...)
    request_message : str = Field(...)
    accept : bool = Field(default=None)
    class Config:
        orm_mode = True
    
