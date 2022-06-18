from typing import Union

from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

class ItemCreate(ItemBase):
    pass