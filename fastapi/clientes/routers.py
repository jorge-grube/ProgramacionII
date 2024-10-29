from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .schemas import DuenoCreate
from .crud import create_dueno
from ..database import get_db

router = APIRouter()

@router.post("/duenos/")
def alta_dueno(dueno: DuenoCreate, db: Session = Depends(get_db)):
    return create_dueno(db, dueno)