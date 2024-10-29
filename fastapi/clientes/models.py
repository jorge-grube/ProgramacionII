from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base  # Cambiado a la nueva importación de SQLAlchemy 2.0

Base = declarative_base()

class Dueno(Base):
    __tablename__ = "duenos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    dni = Column(String(20), unique=True, nullable=False)
    direccion = Column(String(255), nullable=True)
    telefono = Column(String(15), nullable=False)
    correo_electronico = Column(String(100), unique=True, nullable=False)