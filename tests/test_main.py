
import pytest
from fastapi.testclient import TestClient
from app.main import app, Item

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

@pytest.mark.parametrize("item_id,expected_status", [
    (1, 200),
    (50, 200),
    (-1, 400),
    (101, 404)
])
def test_get_item(item_id, expected_status):
    response = client.get(f"/items/{item_id}")
    assert response.status_code == expected_status
    if expected_status == 200:
        assert response.json() == {"item_id": item_id, "name": f"Item {item_id}"}

def test_create_valid_item():
    item_data = {
        "id": 1,
        "name": "Test Item",
        "description": "A test item",
        "price": 10.99
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data

def test_create_invalid_item():
    item_data = {
        "id": 1,
        "name": "Invalid Item",
        "description": "An item with negative price",
        "price": -10.99
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 400
    assert "Price must be positive" in response.json()["detail"]

@pytest.mark.parametrize("user_id,limit,expected_status,expected_length", [
    (1, 5, 200, 5),
    (1, 15, 200, 15),
    (-1, 10, 400, 0),
    (100, 3, 200, 3)
])
def test_get_user_items(user_id, limit, expected_status, expected_length):
    response = client.get(f"/users/{user_id}/items?limit={limit}")
    assert response.status_code == expected_status
    if expected_status == 200:
        items = response.json()
        assert len(items) == expected_length
        assert all(item["owner"] == user_id for item in items)

def test_create_item_missing_fields():
    item_data = {
        "id": 1,
        "name": "Incomplete Item"
        # Missing price field
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 422  # Validation error

def test_get_item_invalid_id_type():
    response = client.get("/items/invalid")
    assert response.status_code == 422  # Validation error
