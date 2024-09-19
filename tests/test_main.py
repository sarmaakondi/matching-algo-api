from fastapi.testclient import TestClient
from main import app
from api import items

# Create a test client instance
client = TestClient(app)


# Test case for get_items endpoint
def test_get_items():
    # Make a GET request to the /api/items endpoint
    response = client.get("/api/items")

    # Assert the status code
    assert response.status_code == 200

    # Assert the response
    data = response.json()
    assert data == items


# Test case for exact match
def test_exact_match():
    # Make a POST request to the /api/match endpoint
    response = client.post(
        "/api/match", json={"trade": "Painting", "unit_of_measure": "M2"}
    )

    # Assert the status code
    assert response.status_code == 200

    # Assert the response
    data = response.json()
    assert data["best_match"]["trade"] == "Painting"
    assert data["best_match"]["unit_of_measure"] == "M2"
    assert data["best_match"]["rate"] == 23
    assert data["similarity_score"] == 1


# Test case for partial match
def test_partial_match():
    # Make a POST request to the /api/match endpoint
    response = client.post(
        "/api/match", json={"trade": "paint", "unit_of_measure": "test"}
    )

    # Assert the status code
    assert response.status_code == 200

    # Assert the response
    data = response.json()
    assert data["best_match"]["trade"] == "Painting"
    assert data["best_match"]["unit_of_measure"] == "HOURS"
    assert data["best_match"]["rate"] == 55
    assert data["similarity_score"] > 0.38


# Test case for no match
def test_no_match():
    # Make a POST request to the /api/match endpoint
    response = client.post(
        "/api/match", json={"trade": "sarma", "unit_of_measure": "incorrect"}
    )

    # Assert the status code
    assert response.status_code == 404

    # Assert the response
    data = response.json()
    assert data == {"detail": "No matching item found for the provided input."}


# Test case for empty input
def test_empty_input():
    # Make a POST request to the /api/match endpoint
    response = client.post(
        "/api/match", json={"trade": "", "unit_of_measure": ""}
    )

    # Assert the status code
    assert response.status_code == 400

    # Assert the response
    data = response.json()
    assert data == {"detail": "'trade' and 'unit_of_measure' cannot be empty."}
