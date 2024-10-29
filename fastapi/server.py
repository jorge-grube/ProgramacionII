from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel as PydanticBaseModel
from typing import List
import pandas as pd
from clientes.endpoints.endpoints import router as clientes_router

# Instancia principal de la aplicación FastAPI
app = FastAPI(
    title="Gestión de Clínica Veterinaria",
    description="API para la gestión de datos de la clínica veterinaria y otras funcionalidades.",
    version="0.2.0",
)

# Incluye el router para los clientes
app.include_router(clientes_router, prefix="/api")

# Clases y funcionalidades adicionales (Contratos, Formularios)
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

# Endpoint para recuperar datos de contratos
@app.get("/retrieve_data/")
def retrieve_data():
    todosmisdatos = pd.read_csv('./contratos_inscritos_simplificado_2023.csv', sep=';')
    todosmisdatos = todosmisdatos.fillna(0)
    todosmisdatosdict = todosmisdatos.to_dict(orient='records')
    listado = ListadoContratos()
    listado.contratos = todosmisdatosdict
    return listado

# Endpoint para envío de formularios
class FormData(BaseModel):
    date: str
    description: str
    option: str
    amount: float

@app.post("/envio/")
async def submit_form(data: FormData):
    return {"message": "Formulario recibido", "data": data}