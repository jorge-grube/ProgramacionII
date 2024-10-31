import shutil
import io
import pandas as pd
from typing import List
from fastapi import FastAPI, File, UploadFile, Form, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel as PydanticBaseModel, EmailStr
from datetime import date, time

# Clases existentes de ejemplo para la funcionalidad de contratos
class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class Contrato(BaseModel):
    fecha: str
    centro_seccion: str
    nreg: str
    nexp: str
    objeto: str
    tipo: str
    procedimiento: str
    numlicit: str
    numinvitcurs: str
    proc_adjud: str
    presupuesto_con_iva: str
    valor_estimado: str
    importe_adj_con_iva: str
    adjuducatario: str
    fecha_formalizacion: str
    I_G: str

class ListadoContratos(BaseModel):
    contratos = List[Contrato]

# Modelo de datos para el alta de clientes
class ClienteCreate(BaseModel):
    nombre: str
    dni: str
    direccion: str
    telefono: str
    correo_electronico: EmailStr

# Modelo de datos para citas
class Appointment(BaseModel):
    client_name: str
    pet_name: str
    date: date
    time: time
    reason: str

# Instancia principal de la aplicación FastAPI
app = FastAPI(
    title="Gestión de Clínica Veterinaria",
    description="""API para la gestión de datos de la clínica veterinaria y otras funcionalidades.""",
    version="0.2.0",
)

# Base de datos en memoria para ejemplo (clientes y citas)
clientes_db = []
appointments_db = []

# Funcionalidades existentes
@app.get("/retrieve_data/")
def retrieve_data():
    todosmisdatos = pd.read_csv('./contratos_inscritos_simplificado_2023.csv', sep=';')
    todosmisdatos = todosmisdatos.fillna(0)
    todosmisdatosdict = todosmisdatos.to_dict(orient='records')
    listado = ListadoContratos()
    listado.contratos = todosmisdatosdict
    return listado

class FormData(BaseModel):
    date: str
    description: str
    option: str
    amount: float

@app.post("/envio/")
async def submit_form(data: FormData):
    return {"message": "Formulario recibido", "data": data}

# Endpoints para gestión de clientes
@app.post("/clients", status_code=status.HTTP_201_CREATED)
def create_client(cliente: ClienteCreate):
    clientes_db.append(cliente.dict())
    return {"message": "Dueño registrado exitosamente", "data": cliente}

@app.get("/clients", response_model=List[ClienteCreate])
def get_clients():
    if not clientes_db:
        raise HTTPException(status_code=404, detail="No hay dueños registrados")
    return clientes_db

@app.put("/clients/{dni}", status_code=status.HTTP_200_OK)
def update_client(dni: str, updated_cliente: ClienteCreate):
    for i, cliente in enumerate(clientes_db):
        if cliente["dni"] == dni:
            clientes_db[i] = updated_cliente.dict()
            return {"message": "Dueño actualizado exitosamente", "data": updated_cliente}
    raise HTTPException(status_code=404, detail="Dueño no encontrado")

@app.delete("/clients/{dni}", status_code=status.HTTP_200_OK)
def delete_client(dni: str):
    for i, cliente in enumerate(clientes_db):
        if cliente["dni"] == dni:
            clientes_db.pop(i)
            return {"message": "Dueño eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Dueño no encontrado")

# Endpoints para gestión de citas
@app.post("/appointments", status_code=status.HTTP_201_CREATED)
def create_appointment(appointment: Appointment):
    appointments_db.append(appointment.dict())
    return {"message": "Cita creada exitosamente", "data": appointment}

@app.get("/appointments", response_model=List[Appointment])
def get_appointments():
    if not appointments_db:
        raise HTTPException(status_code=404, detail="No hay citas registradas")
    return appointments_db

@app.put("/appointments/{appointment_id}", status_code=status.HTTP_200_OK)
def update_appointment(appointment_id: int, updated_appointment: Appointment):
    if 0 <= appointment_id < len(appointments_db):
        appointments_db[appointment_id] = updated_appointment.dict()
        return {"message": "Cita actualizada exitosamente", "data": updated_appointment}
    raise HTTPException(status_code=404, detail="Cita no encontrada")

@app.delete("/appointments/{appointment_id}", status_code=status.HTTP_200_OK)
def delete_appointment(appointment_id: int):
    if 0 <= appointment_id < len(appointments_db):
        appointments_db.pop(appointment_id)
        return {"message": "Cita eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Cita no encontrada")