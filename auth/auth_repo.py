from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
from . import  auth_schemas
import models

def register(user: auth_schemas.UserInDB, db: Session):
    db_user = models.User(username=user['username'],email=user['email'],password=user['password'])
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_certain_user(db:Session, username: str):
    user= db.query(models.User).filter(models.User.username == username).first()
    if user is not None:
        return auth_schemas.UserInDB(username=user.username,email=user.email,password=user.password)
    else:
        return None

