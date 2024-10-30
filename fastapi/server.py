from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from veterinaria.clientes.models import Dueño, Base
from veterinaria.clientes.schema import DueñoCreate

DATABASE_URL = "sqlite:///./recetas.db"  # Ajusta esta URL si es necesario
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas en la base de datos si aún no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/alta_dueño/")
async def alta_dueño(dueño: DueñoCreate, db: Session = Depends(get_db)):
    db_dueño = Dueño(
        nombre=dueño.nombre,
        dni=dueño.dni,
        direccion=dueño.direccion,
        telefono=dueño.telefono,
        correo_electronico=dueño.correo_electronico
    )
    db.add(db_dueño)
    db.commit()
    db.refresh(db_dueño)
    return db_dueño
