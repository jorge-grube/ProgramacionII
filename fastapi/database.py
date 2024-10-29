from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Crear la conexión a la base de datos (asegúrate de ajustar la URL de la base de datos según tus necesidades)
DATABASE_URL = "sqlite:///./test.db"  # Cambia esto a la URL de tu base de datos real
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia de base de datos para obtener sesiones
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()