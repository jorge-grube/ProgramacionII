from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List
from datetime import date, time

router = APIRouter()

# Modelo de datos para citas
class Appointment(BaseModel):
    client_name: str
    pet_name: str
    date: date
    time: time
    reason: str

# Base de datos en memoria (para ejemplo)
appointments_db = []

@router.post("/appointments", status_code=status.HTTP_201_CREATED)
def create_appointment(appointment: Appointment):
    appointments_db.append(appointment.dict())
    return {"message": "Cita creada exitosamente", "data": appointment}

@router.get("/appointments", response_model=List[Appointment])
def get_appointments():
    if not appointments_db:
        raise HTTPException(status_code=404, detail="No hay citas registradas")
    return appointments_db

@router.put("/appointments/{appointment_id}", status_code=status.HTTP_200_OK)
def update_appointment(appointment_id: int, updated_appointment: Appointment):
    if 0 <= appointment_id < len(appointments_db):
        appointments_db[appointment_id] = updated_appointment.dict()
        return {"message": "Cita actualizada exitosamente", "data": updated_appointment}
    raise HTTPException(status_code=404, detail="Cita no encontrada")

@router.delete("/appointments/{appointment_id}", status_code=status.HTTP_200_OK)
def delete_appointment(appointment_id: int):
    if 0 <= appointment_id < len(appointments_db):
        appointments_db.pop(appointment_id)
        return {"message": "Cita eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Cita no encontrada")