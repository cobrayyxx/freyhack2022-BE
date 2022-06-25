from sqlalchemy.orm import Session
from . import request_schemas
import models
from sqlalchemy import update
from fastapi.exceptions import HTTPException

def create_request(db:Session, request:request_schemas.Request):
    db_request_item = models.Request(**request.dict())
    db.add(db_request_item)
    db.commit()
    db.refresh(db_request_item)
    return db_request_item

def get_certain_request_by_id(db:Session, request_id:int):
    return db.query(models.Request).filter(models.Request.id == int(request_id)).first()

def accept_request(db:Session, request_id:int, request:request_schemas.RequestUpdate):
    db_req = get_certain_request_by_id(db, request_id)

    if db_req is None:
        raise HTTPException(status_code=404, detail="Request not found")
    
    req_data = request.dict(exclude_unset=True)
    for key, value in req_data.items():
        setattr(db_req, key, value)
    
    db.add(db_req)
    db.commit()
    db.refresh(db_req)
    return db_req

def reject_request(db:Session, request_id:int):
    db_req = get_certain_request_by_id(db, request_id)

    if db_req is None:
        raise HTTPException(status_code=404, detail="Request not found")
    
    db.delete(db_req)
    return True

    

