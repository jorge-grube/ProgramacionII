from pydantic import BaseModel

class DuenoCreate(BaseModel):
    nombre: str
    dni: str
    direccion: str
    telefono: str
    correo: str