import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config.settings import settings
client = TestClient(app)

def test_version_printing():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == settings.VERSION

def test_temperature():
    response = client.get("/temperature")
    assert response.status_code == 200
    isinstance(response.json().value(),float)