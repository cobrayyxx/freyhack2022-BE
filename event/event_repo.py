from . import event_schemas
import models
from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db

def create_event(db:Session, event:event_schemas.Event):
    db_event_item = models.Event(**event.dict())
    db.add(db_event_item)
    db.commit()
    db.refresh(db_event_item)
    return db_event_item

def get_events(db: Session= Depends(get_db), skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()

def get_events_by_id(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == int(event_id)).first()

def search_event_db(db: Session, query: str):
    events = db.query(models.Event).filter(models.Event.name.contains(query)).all()
    return events