from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime

router = APIRouter()

# Modelo de datos para clientes
class ClienteCreate(BaseModel):
    nombre: str
    dni: str
    direccion: str
    telefono: str
    correo_electronico: EmailStr

# Base de datos en memoria (para ejemplo)
clientes_db = []

@router.post("/clients", status_code=status.HTTP_201_CREATED)
def create_client(cliente: ClienteCreate):
    clientes_db.append(cliente.dict())
    return {"message": "Dueño registrado exitosamente", "data": cliente}

@router.get("/clients", response_model=List[ClienteCreate])
def get_clients():
    if not clientes_db:
        raise HTTPException(status_code=404, detail="No hay dueños registrados")
    return clientes_db

@router.put("/clients/{dni}", status_code=status.HTTP_200_OK)
def update_client(dni: str, updated_cliente: ClienteCreate):
    for i, cliente in enumerate(clientes_db):
        if cliente["dni"] == dni:
            clientes_db[i] = updated_cliente.dict()
            return {"message": "Dueño actualizado exitosamente", "data": updated_cliente}
    raise HTTPException(status_code=404, detail="Dueño no encontrado")

@router.delete("/clients/{dni}", status_code=status.HTTP_200_OK)
def delete_client(dni: str):
    for i, cliente in enumerate(clientes_db):
        if cliente["dni"] == dni:
            clientes_db.pop(i)
            return {"message": "Dueño eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Dueño no encontrado")