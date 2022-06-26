from fastapi import Depends, FastAPI

from auth import auth_controller
from event import event_controller
from request import request_controller
import models
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
   "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(auth_controller.router)
app.include_router(event_controller.router)
app.include_router(request_controller.router)

