from fastapi.testclient import TestClient
from app import app   # this imports your FastAPI app from app.py

client = TestClient(app)

def test_home_welcome_message():
    """Check that the root endpoint returns the expected welcome message"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "GIC Python Assessment API is running!"}

def test_health_endpoint():
    """Check that /health returns 200 and correct JSON"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

