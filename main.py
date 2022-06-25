from fastapi import Depends, FastAPI

from auth import auth_controller
from event import event_controller
import models
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth_controller.router)
app.include_router(event_controller.router)
