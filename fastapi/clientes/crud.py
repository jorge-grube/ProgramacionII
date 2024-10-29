from sqlalchemy.orm import Session
from .models import Dueno
from .schemas import DuenoCreate

def create_dueno(db: Session, dueno: DuenoCreate):
    db_dueno = Dueno(
        nombre=dueno.nombre,
        dni=dueno.dni,
        direccion=dueno.direccion,
        telefono=dueno.telefono,
        correo_electronico=dueno.correo_electronico,
    )
    db.add(db_dueno)
    db.commit()
    db.refresh(db_dueno)
    return db_dueno