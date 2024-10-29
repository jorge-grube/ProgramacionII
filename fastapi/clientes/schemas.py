from pydantic import BaseModel, EmailStr
from typing import Optional

class DuenoCreate(BaseModel):
    nombre: str
    dni: str
    direccion: Optional[str] = None
    telefono: str
    correo_electronico: EmailStr