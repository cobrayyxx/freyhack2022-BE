from fastapi import Depends, FastAPI

from sub_app1 import users
from sub_app2 import items

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
