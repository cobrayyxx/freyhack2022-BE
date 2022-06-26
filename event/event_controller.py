from threading import currentThread
from fastapi import APIRouter, Depends
from . import event_schemas
from . import event_repo
from sqlalchemy.orm import Session
from database import get_db
from auth.auth_schemas import User
from auth.auth_controller import get_current_active_user
from typing import Optional

router = APIRouter(
    prefix="/api/v1",
    tags=["event"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/event", response_model=event_schemas.Event)
def create_event( event: event_schemas.Event, current_user: User = Depends(get_current_active_user), db: Session=Depends(get_db)):
    event.creator = current_user.username
    return event_repo.create_event(db=db, event=event)

@router.get("/event", response_model=list[event_schemas.Event])
def get_all_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),current_user: User = Depends(get_current_active_user)):
    events = event_repo.get_events(db, skip=skip, limit=limit)
    return events

@router.get("/events/{event_id}", response_model=event_schemas.Event)
def get_certain_event(event_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_active_user)):
    event = event_repo.get_events_by_id(db, event_id)
    return event

@router.get("/search/", response_model=list[event_schemas.Event])
def search_event(db: Session = Depends(get_db), query: Optional[str] = None):
    events = event_repo.search_event_db(db, query)
    return events