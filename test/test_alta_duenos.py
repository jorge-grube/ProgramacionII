from fastapi.testclient import TestClient
from server import app
import pytest

client = TestClient(app)

@pytest.fixture
def nuevo_dueno():
    return {
        "nombre": "Juan Perez",
        "dni": "12345678Z",
        "direccion": "Calle Falsa 123",
        "telefono": "123456789",
        "correo_electronico": "juan.perez@example.com"
    }

def test_alta_dueno_exitoso(nuevo_dueno):
    response = client.post("/clientes/duenos/", json=nuevo_dueno)
    assert response.status_code == 200
    assert response.json()["nombre"] == nuevo_dueno["nombre"]

def test_alta_dueno_dni_repetido(nuevo_dueno):
    client.post("/clientes/duenos/", json=nuevo_dueno)
    response = client.post("/clientes/duenos/", json=nuevo_dueno)
    assert response.status_code == 400
    assert response.json()["detail"] == "Error al crear el dueño"

def test_alta_dueno_correo_invalido():
    dueno = {
        "nombre": "Carlos Lopez",
        "dni": "87654321X",
        "direccion": "Avenida Siempre Viva 742",
        "telefono": "987654321",
        "correo_electronico": "correo_invalido"
    }
    response = client.post("/clientes/duenos/", json=dueno)
    assert response.status_code == 422