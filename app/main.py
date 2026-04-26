import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Dog Breed API")
JSON_FILE = "dogs.json"

# --- Data Models ---

class Image(BaseModel):
    id: str
    width: int
    height: int
    url: str

class Measurement(BaseModel):
    imperial: str
    metric: str

class DogBreed(BaseModel):
    id: int
    name: str
    weight: Optional[Measurement] = None
    height: Optional[Measurement] = None
    bred_for: Optional[str] = None
    breed_group: Optional[str] = None
    life_span: Optional[str] = None
    temperament: Optional[str] = None
    origin: Optional[str] = None
    reference_image_id: Optional[str] = None
    image: Optional[Image] = None

# --- Helper Functions ---

def load_data() -> List[dict]:
    # CHANGE: Use JSON_FILE variable instead of "dogs.json"
    if not os.path.exists(JSON_FILE): 
        return []
    with open(JSON_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(data: List[dict]):
    # CHANGE: Use the variable JSON_FILE, not the string "dogs.json"
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- Endpoints ---

@app.get("/breeds", response_model=List[DogBreed])
def get_all_breeds():
    """Read: Returns all dog breeds."""
    return load_data()

@app.get("/breeds/{breed_id}", response_model=DogBreed)
def get_breed(breed_id: int):
    """Read: Returns a specific breed by ID."""
    data = load_data()
    breed = next((b for b in data if b["id"] == breed_id), None)
    if not breed:
        raise HTTPException(status_code=404, detail="Breed not found")
    return breed

@app.post("/breeds", status_code=201, response_model=DogBreed)
def create_breed(breed: DogBreed):
    """Create: Adds a new dog breed to the file."""
    data = load_data()
    if any(b["id"] == breed.id for b in data):
        raise HTTPException(status_code=400, detail="Breed ID already exists")
    
    new_breed = breed.dict()
    data.append(new_breed)
    save_data(data)
    return new_breed

@app.put("/breeds/{breed_id}", response_model=DogBreed)
def update_breed(breed_id: int, updated_breed: DogBreed):
    """Update: Modifies an existing breed in the file."""
    data = load_data()
    index = next((i for i, b in enumerate(data) if b["id"] == breed_id), None)
    
    if index is None:
        raise HTTPException(status_code=404, detail="Breed not found")
    
    data[index] = updated_breed.dict()
    save_data(data)
    return data[index]

@app.delete("/breeds/{breed_id}")
def delete_breed(breed_id: int):
    """Delete: Removes a breed from the file."""
    data = load_data()
    original_len = len(data)
    data = [b for b in data if b["id"] != breed_id]
    
    if len(data) == original_len:
        raise HTTPException(status_code=404, detail="Breed not found")
    
    save_data(data)
    return {"detail": f"Breed {breed_id} deleted successfully"}
