from fastapi import FastAPI
from clientes.routers import router as duenos_router

# Instancia principal de la aplicación FastAPI
app = FastAPI(
    title="Gestión de Clínica Veterinaria",
    description="API para la gestión de datos de la clínica veterinaria.",
    version="0.2.0",
)

# Incluir el router de dueños con el prefijo "/clientes"
app.include_router(duenos_router, prefix="/clientes")