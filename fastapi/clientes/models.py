from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dueno(Base):
    __tablename__ = "duenos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    dni = Column(String, unique=True, index=True)
    direccion = Column(String)
    telefono = Column(String)
    correo_electronico = Column(String, unique=True)