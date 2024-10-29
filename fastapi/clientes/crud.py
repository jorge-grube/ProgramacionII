from sqlalchemy.orm import Session
from . import models, schemas

def create_dueno(db: Session, dueno: schemas.DuenoCreate):
    db_dueno = models.Dueno(
        nombre=dueno.nombre,
        dni=dueno.dni,
        direccion=dueno.direccion,
        telefono=dueno.telefono,
        correo_electronico=dueno.correo_electronico
    )
    db.add(db_dueno)
    db.commit()
    db.refresh(db_dueno)
    return db_dueno