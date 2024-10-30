from pydantic import BaseModel, EmailStr

class DueñoCreate(BaseModel):
    nombre: str
    dni: str
    direccion: str
    telefono: str
    correo_electronico: EmailStr