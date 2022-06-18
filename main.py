from fastapi import Depends, FastAPI

from sub_app1 import users
from sub_app2 import items
import models
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(items.router)
