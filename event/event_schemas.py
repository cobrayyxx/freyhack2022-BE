from typing import Union

from pydantic import BaseModel, Field
from datetime import datetime

class Event(BaseModel):
    id: int = Field(None)
    creator: str = Field(...)
    name: str = Field(...)
    latitude: int = Field(None)
    longitude: int = Field(None)
    location: str = Field(...)
    description: str = Field(..., max_length=500)
    contact: str=Field(...)
    num_participants: int=Field(default=0)
    datetime: int=Field(...)
    class Config:
        orm_mode = True
