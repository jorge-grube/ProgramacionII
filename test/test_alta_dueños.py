from fastapi.testclient import TestClient
from fastapi.server import app

client = TestClient(app)

def test_alta_dueño():
    response = client.post("/alta_dueño/", json={
        "nombre": "Ana López",
        "dni": "12345678Z",
        "direccion": "Calle Principal 12",
        "telefono": "555678901",
        "correo_electronico": "ana.lopez@example.com"
    })
    assert response.status_code == 200
    assert response.json()["nombre"] == "Ana López"