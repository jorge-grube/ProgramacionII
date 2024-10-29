import pandas as pd
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel as PydanticBaseModel

# Importar el router del módulo clientes (dueños)
from clientes.routers import router as duenos_router

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
    contratos: List[Contrato] = []

# Instancia principal de la aplicación FastAPI
app = FastAPI(
    title="Gestión de Clínica Veterinaria",
    description="API para la gestión de datos de la clínica veterinaria y otras funcionalidades.",
    version="0.2.0",
)

# Incluir el router de dueños con el prefijo "/clientes"
app.include_router(duenos_router, prefix="/clientes")

# Endpoint para recuperar datos de contratos (funcionalidad existente)
@app.get("/retrieve_data/")
def retrieve_data():
    # Leer el archivo CSV (asegúrate de que la ruta es correcta)
    try:
        todosmisdatos = pd.read_csv('./contratos_inscritos_simplificado_2023.csv', sep=';')
        todosmisdatos = todosmisdatos.fillna(0)
        todosmisdatosdict = todosmisdatos.to_dict(orient='records')
        listado = ListadoContratos()
        listado.contratos = [Contrato(**contrato) for contrato in todosmisdatosdict]
        return listado
    except FileNotFoundError:
        return {"error": "El archivo de datos no fue encontrado"}
    except Exception as e:
        return {"error": str(e)}

# Endpoint para envío de formularios (funcionalidad de ejemplo)
class FormData(PydanticBaseModel):
    date: str
    description: str
    option: str
    amount: float

@app.post("/envio/")
async def submit_form(data: FormData):
    return {"message": "Formulario recibido", "data": data.dict()}