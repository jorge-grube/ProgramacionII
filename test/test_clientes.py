from fastapi.testclient import TestClient
from fastapi.server import app  # Asegúrate de que la ruta de importación sea correcta

client = TestClient(app)

def test_crear_dueno():
    response = client.post(
        "/api/duenos/",
        json={
            "nombre": "Carlos",
            "dni": "12345678Z",
            "direccion": "Calle Falsa 123",
            "telefono": "123456789",
            "correo": "carlos@mail.com"
        }
    )
    assert response.status_code == 200
    assert response.json()["nombre"] == "Carlos"