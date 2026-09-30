import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_register_customer(client):
    response = client.post(
        "/customers",
        json={"name": "Ajay", "email": "ajay@example.com"}
    )
    assert response.status_code == 201


def test_get_customers(client):
    response = client.get("/customers")
    assert response.status_code == 200