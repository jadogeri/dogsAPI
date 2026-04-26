import json
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your code is in main.py
import main

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_and_teardown(tmp_path):
    # Create a temporary file path for testing
    test_json = tmp_path / "dogs.json"

    # Mock the JSON_FILE path in your main module to use this temp file
    old_file_path = main.JSON_FILE
    main.JSON_FILE = str(test_json)

    # Seed data
    sample_data = [
        {"id": 1, "name": "Golden Retriever", "temperament": "Friendly"},
        {"id": 2, "name": "Beagle", "temperament": "Curious"}
    ]

    with open(main.JSON_FILE, "w") as f:
        json.dump(sample_data, f)

    yield

    # Restore the original file path configuration
    main.JSON_FILE = old_file_path


def test_get_all_breeds():
    response = client.get("/breeds")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    # Fixed index access from previous snippet
    assert data[0]["name"] == "Golden Retriever"


def test_get_breed_success():
    response = client.get("/breeds/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Golden Retriever"


def test_get_breed_not_found():
    response = client.get("/breeds/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Breed not found"


def test_create_breed_success():
    new_dog = {
        "id": 3,
        "name": "Poodle",
        "temperament": "Intelligent"
    }
    response = client.post("/breeds", json=new_dog)
    assert response.status_code == 201
    assert response.json()["name"] == "Poodle"

    # Double-check persistence
    get_response = client.get("/breeds/3")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Poodle"


def test_create_breed_duplicate_id():
    # Use a complete model to avoid Pydantic validation errors
    duplicate_dog = {
        "id": 1,
        "name": "Fake Golden",
        "temperament": "Mean"
    }
    response = client.post("/breeds", json=duplicate_dog)
    assert response.status_code == 400
    assert response.json()["detail"] == "Breed ID already exists"
