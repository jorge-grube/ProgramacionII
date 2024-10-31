import pytest
from unittest.mock import patch
import pandas as pd
import sys

# Añadir la ruta donde se encuentra appointments.py
sys.path.insert(0, "/home/jorge_grube/ProgramacionII/streamlit/pages")

# Importar las funciones de appointments
from appointments import get_appointments, create_appointment, update_appointment, delete_appointment

# Prueba para obtener citas
@patch("appointments.requests.get")
def test_get_appointments(mock_get):
    # Simular la respuesta de la API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"client_name": "Juan", "pet_name": "Max", "date": "2023-12-01", "time": "10:00", "reason": "Vacunación"}
    ]
    # Llamar a la función y verificar el resultado
    result = get_appointments()
    assert not result.empty
    assert isinstance(result, pd.DataFrame)

# Prueba para crear una cita
@patch("appointments.requests.post")
def test_create_appointment(mock_post):
    # Simular la respuesta de la API
    mock_post.return_value.status_code = 201
    # Llamar a la función y verificar que se haya llamado al mock
    create_appointment("Ana", "Luna", "2023-12-02", "11:00", "Revisión")
    assert mock_post.called

# Prueba para actualizar una cita
@patch("appointments.requests.put")
def test_update_appointment(mock_put):
    # Simular la respuesta de la API
    mock_put.return_value.status_code = 200
    # Llamar a la función y verificar que se haya llamado al mock
    update_appointment(1, "Carlos", "Nala", "2023-12-03", "12:00", "Desparasitación")
    assert mock_put.called

# Prueba para eliminar una cita
@patch("appointments.requests.delete")
def test_delete_appointment(mock_delete):
    # Simular la respuesta de la API
    mock_delete.return_value.status_code = 200
    # Llamar a la función y verificar que se haya llamado al mock
