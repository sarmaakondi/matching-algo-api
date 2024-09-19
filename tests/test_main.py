from fastapi.testclient import TestClient
from main import app
from api import items

# Create a test client instance
client = TestClient(app)


# Test get_items endpoint
def test_get_items():
    # Make a GET request to the /api/items endpoint
    response = client.get("/api/items")

    # Assert the status code
    assert response.status_code == 200

    # Asser the response
    data = response.json()
    assert data == items
