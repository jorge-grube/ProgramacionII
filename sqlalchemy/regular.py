from veterinaria.clientes.models import Dueño, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import logging

if __name__ == '__main__':
    try:
        dbname = 'recetas.db'
        engine = create_engine('sqlite:///' + dbname, echo=True)
        Base.metadata.create_all(bind=engine)
        with Session(engine) as session:
            # Ejemplo de inserción
            nuevo_dueño = Dueño(nombre="Carlos García", dni="87654321X", direccion="Calle Real 45", telefono="555432123", correo_electronico="carlos.garcia@example.com")
            session.add(nuevo_dueño)
            session.commit()

            logging.info("Alta de dueño exitosa")
    except Exception as e:
        logging.error(e.args)
        session.rollback()
    finally:
        session.close()