from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import Dueno
from .schemas import DuenoCreate
from database import get_db  # Asegúrate de tener la función get_db configurada en tu proyecto

router = APIRouter()

@router.post("/duenos/")
def crear_dueno(dueno: DuenoCreate, db: Session = Depends(get_db)):
    db_dueno = Dueno(**dueno.dict())
    db.add(db_dueno)
    try:
        db.commit()
        db.refresh(db_dueno)
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el dueño")
    return db_dueno