from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Request(BaseModel):
    id: int = Field(None)
    event_id : int = Field(...)
    requester_id : str = Field(...)
    request_message : str = Field(...)
    accept : bool = Field(default=None)

    class Config:
        orm_mode = True
    
class RequestUpdate(BaseModel):
    accept: Optional[bool]

class Enrolled(BaseModel):
    event_id: int = Field(...)
    username: str = Field(...)
    class Config:
        orm_mode = True