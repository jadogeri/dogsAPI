# 🚀 FastAPI Dog Breed CRUD API

**Author:** Joseph Adogeri

**Version:** 1.0

**Date:** April 26, 2026

<div align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI Logo" width="400">
</div>

---

## Description

A high-performance Python FastAPI CRUD (Create, Read, Update, Delete) API for managing dog breed information. This project features automatic Pydantic data validation and serves data directly from a local JSON persistence layer.

---

## 🛠 Tech Stack

*   **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
*   **Validation:** [Pydantic](https://pydantic.dev)
*   **Server:** [Uvicorn](https://uvicorn.org)
*   **Package Manager:** Pip (via `pyproject.toml`)
*   **Database:** JSON (Local File Persistence)
*   **API Documentation:** Interactive Swagger UI & ReDoc (Built-in)

---

## 📦 Installation & Setup 
Note: Command references are available in `commands.txt`

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    cd dog_breeds_api
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install project & dependencies:**
    ```bash
    pip install .
    # Or for development (editable mode):
    pip install -e .
    ```

4.  **Run the application:**
    ```bash
    # Using the script defined in pyproject.toml
    start-dog-api
    # Or using standard uvicorn
    uvicorn main:app --reload
    ```

---

## 📖 API Documentation (Swagger)

Once the server is running, access the interactive documentation at:

*   **Swagger UI:** `http://localhost:8000/docs`
*   **ReDoc:** `http://localhost:8000/redoc`

---

## 🛣 API Endpoints


| Method  | Endpoint | Description |
| :--- | :--- | :--- |
| 📥 **GET** | `/breeds` | **Get All:** Retrieve a list of all dog breeds |
| 🔍 **GET** | `/breeds/{id}` | **Get One:** Retrieve details for a specific breed by ID |
| ✨ **POST** | `/breeds` | **Create:** Add a new dog breed with JSON payload |
| 🔄 **PUT** | `/breeds/{id}` | **Update:** Modify existing breed information |
| 🗑️ **DELETE** | `/breeds/{id}` | **Delete:** Remove a breed from the system |

---

## 🧪 Testing with REST Client

You can test the API endpoints using the `test_main.http` file. If you are using VS Code, install the **REST Client** extension to run these requests directly.

```http

### Get a specific breed
GET http://localhost:8000//1
Accept: application/json

HTTP/1.1 200 OK
date: Sun, 26 Apr 2026 15:47:40 GMT
server: uvicorn
content-length: 467
content-type: application/json

{
  "id": 1,
  "name": "Affenpinscher",
  "weight": {
    "imperial": "6 - 13",
    "metric": "3 - 6"
  },
  "height": {
    "imperial": "9 - 11.5",
    "metric": "23 - 29"
  },
  "bred_for": "Small rodent hunting, lapdog",
  "breed_group": "Toy",
  "life_span": "10 - 12 years",
  "temperament": "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving",
  "origin": "Germany, France",
  "reference_image_id": "BJa4kxc4X",
  "image": {
    "id": "BJa4kxc4X",
    "width": 1600,
    "height": 1199,
    "url": "https://cdn2.thedogapi.com/images/BJa4kxc4X.jpg"
  }
}


```

---

## 📄 Project Structure

```text
📂 dog-breed-api/ (Root)
├── 📂 .github/workflows/       # 🤖 GitHub Actions CI Configuration
├── 📂 .venv/                   # 🐍 Python Virtual Environment
├── 📄 dogs.json                # 🗄️ JSON database file
├── 📄 main.py                  # 🚀 FastAPI entry point & CRUD logic
├── 📄 README.md                # 📖 Project documentation
├── 📄 pyproject.toml           # 📦 Modern project configuration
├── 📄 commands.txt             # ⌨️ CLI Command reference
└── 📄 test_main.http           # ⚡ REST Client test file
```
