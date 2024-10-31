import pytest
import utils.api_utils as api

# Prueba para la creación de clientes
def test_create_client(monkeypatch):
    def mock_post(url, json):
        class MockResponse:
            status_code = 201
            def json(self):
                return {"message": "Success"}
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)
    success, message = api.create_client({
        "nombre": "Test Name",
        "dni": "12345678X",
        "direccion": "Test Address",
        "telefono": "600123456",
        "correo_electronico": "test@example.com"
    })
    assert success == True
    assert message == "Dueño registrado exitosamente"

# Prueba para la actualización de clientes
def test_update_client(monkeypatch):
    def mock_put(url, json):
        class MockResponse:
            status_code = 200
            def json(self):
                return {"message": "Success"}
        return MockResponse()

    monkeypatch.setattr("requests.put", mock_put)
    success, message = api.update_client("12345678X", {
        "nombre": "Updated Name",
        "dni": "12345678X",
        "direccion": "Updated Address",
        "telefono": "600654321",
        "correo_electronico": "updated@example.com"
    })
    assert success == True
    assert message == "Dueño actualizado exitosamente"

# Prueba para la eliminación de clientes
def test_delete_client(monkeypatch):
    def mock_delete(url):
        class MockResponse:
            status_code = 200
        return MockResponse()

    monkeypatch.setattr("requests.delete", mock_delete)
    success, message = api.delete_client("12345678X")
    assert success == True
    assert message == "Dueño eliminado exitosamente"

# Prueba para la creación de citas
def test_create_appointment(monkeypatch):
    def mock_post(url, json):
        class MockResponse:
            status_code = 201
            def json(self):
                return {"message": "Success"}
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)
    success, message = api.create_appointment({
        "client_name": "Test Client",
        "pet_name": "Test Pet",
        "date": "2024-10-31",
        "time": "10:30",
        "reason": "Routine Checkup"
    })
    assert success == True
    assert message == "Cita creada exitosamente"

# Prueba para la actualización de citas
def test_update_appointment(monkeypatch):
    def mock_put(url, json):
        class MockResponse:
            status_code = 200
            def json(self):
                return {"message": "Success"}
        return MockResponse()

    monkeypatch.setattr("requests.put", mock_put)
    success, message = api.update_appointment(1, {
        "client_name": "Updated Client",
        "pet_name": "Updated Pet",
        "date": "2024-11-01",
        "time": "15:00",
        "reason": "Updated Checkup"
    })
    assert success == True
    assert message == "Cita actualizada exitosamente"

# Prueba para la eliminación de citas
def test_delete_appointment(monkeypatch):
    def mock_delete(url):
        class MockResponse:
            status_code = 200
        return MockResponse()

    monkeypatch.setattr("requests.delete", mock_delete)
    success, message = api.delete_appointment(1)
    assert success == True
    assert message == "Cita eliminada exitosamente"