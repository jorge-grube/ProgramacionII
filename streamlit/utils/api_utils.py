import requests
import pandas as pd

API_BASE_URL = "http://localhost:8000"

# Función para crear un nuevo cliente
def create_client(data):
    response = requests.post(f"{API_BASE_URL}/clients", json=data)
    if response.status_code == 201:
        return True, "Dueño registrado exitosamente"
    else:
        return False, f"Error al registrar el dueño: {response.text}"

# Función para obtener todos los clientes
def get_clients():
    response = requests.get(f"{API_BASE_URL}/clients")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Error al cargar los dueños: {response.text}")

# Función para crear una cita
def create_appointment(data):
    response = requests.post(f"{API_BASE_URL}/appointments", json=data)
    if response.status_code == 201:
        return True, "Cita creada exitosamente"
    else:
        return False, f"Error al crear la cita: {response.text}"

# Función para actualizar una cita
def update_appointment(appointment_id, data):
    response = requests.put(f"{API_BASE_URL}/appointments/{appointment_id}", json=data)
    if response.status_code == 200:
        return True, "Cita actualizada exitosamente"
    else:
        return False, f"Error al actualizar la cita: {response.text}"

# Función para eliminar una cita
def delete_appointment(appointment_id):
    response = requests.delete(f"{API_BASE_URL}/appointments/{appointment_id}")
    if response.status_code == 200:
        return True, "Cita eliminada exitosamente"
    else:
        return False, f"Error al eliminar la cita: {response.text}"

# Función para actualizar un cliente
def update_client(dni, data):
    response = requests.put(f"{API_BASE_URL}/clients/{dni}", json=data)
    if response.status_code == 200:
        return True, "Dueño actualizado exitosamente"
    else:
        return False, f"Error al actualizar el dueño: {response.text}"

# Función para eliminar un cliente
def delete_client(dni):
    response = requests.delete(f"{API_BASE_URL}/clients/{dni}")
    if response.status_code == 200:
        return True, "Dueño eliminado exitosamente"
    else:
        return False, f"Error al eliminar el dueño: {response.text}"