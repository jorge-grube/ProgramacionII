from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud
from ..database import get_db  # Asegúrate de tener configurado el get_db para acceder a la base de datos

router = APIRouter()

@router.post("/duenos/", response_model=schemas.DuenoCreate)
def create_dueno(dueno: schemas.DuenoCreate, db: Session = Depends(get_db)):
    db_dueno = crud.create_dueno(db=db, dueno=dueno)
    if not db_dueno:
        raise HTTPException(status_code=400, detail="Error al crear el dueño")
    return db_dueno