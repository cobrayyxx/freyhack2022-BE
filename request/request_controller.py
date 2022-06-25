from fastapi import APIRouter, Depends
from . import request_schemas, request_repo
from auth.auth_schemas import User
from auth.auth_controller import get_current_active_user
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix="/api/v1",
    tags=["request"],
    responses={404: {"description": "Not found"}},
)

@router.post("/request")
def create_request_controller(request:request_schemas.Request, 
    current_user: User = Depends(get_current_active_user), db: Session=Depends(get_db)):
    return request_repo.create_request(db, request)

@router.put("/request/acc/{request_id}")
def accept_request_controller(request:request_schemas.RequestUpdate, request_id: int, 
    db:Session=Depends(get_db),  current_user: User = Depends(get_current_active_user)):
    print(request)
    return request_repo.accept_request(db, request_id, request)

@router.delete("/request/reject/{request_id}")
def reject_request_controller(request_id:int,db:Session=Depends(get_db), 
    current_user: User = Depends(get_current_active_user)):
    return request_repo.reject_request(db, request_id)