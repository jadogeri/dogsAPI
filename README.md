# 🚀 FastAPI Dog Breed CRUD API

**Author:** Joseph Adogeri
<br/>
**Version:** 1.0
<br/>
**Date:** April 26, 2026

<div align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI Logo" width="400">
</div>

---

## Description

A high-performance Python FastAPI CRUD (Create, Read, Update, Delete) API for managing dog breed information. This project features automatic Pydantic data validation and serves data directly from a local JSON persistence layer.

---

## 📍 Table of Contents

*   [🛠 Tech Stack](#-tech-stack)
*   [📦 Installation & Setup](#-installation--setup)
*   [📖 API Documentation](#-api-documentation-swagger)
*   [🛣 API Endpoints](#-api-endpoints)
*   [🧪 Testing with REST Client](#-testing-with-rest-client)
*   [🧠 Post-Mortem: Challenges & Learning](#-post-mortem-challenges--learning)
*   [🚀 Future Roadmap](#-future-roadmap-scaling-the-project)
*   [📄 Project Structure](#-project-structure)
*   [📄 License](#-license)

---

## 🛠 Tech Stack

*   **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
*   **Validation:** [Pydantic](https://pydantic.dev)
*   **Server:** [Uvicorn](https://uvicorn.org)
*   **Package Manager:** Pip (via `pyproject.toml`)
*   **Database:** JSON (Local File Persistence)
*   **CI/CD:** GitHub Actions (Automated Pytest & Flake8)
*   **API Documentation:** Interactive Swagger UI & ReDoc (Built-in)

---

## 📦 Installation & Setup 
Note: Command references are available in `commands.txt`

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    cd dog-breed-api
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install project & dependencies:**
    ```bash
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

---

## 🧠 Post-Mortem: Challenges & Learning

### 🛠 Key Challenges & Solutions
*   **Automated Testing in CI/CD:** A major hurdle was configuring GitHub Actions to recognize the project root while tests were in a sub-directory. 
    *   *Solution:* I overcame this by modernizing the `pyproject.toml` with `pythonpath = ["."]` and utilizing `pip install -e .` to ensure the local module was correctly installed in the virtual environment during the build process.
*   **Stateless Persistence:** Managing a local JSON file as a database requires careful handling of file I/O to prevent data corruption during concurrent writes.
    *   *Solution:* Implemented helper functions to encapsulate the `json` serialization logic, ensuring a consistent state between the API memory and the physical file.

### 🎓 Lessons Learned
*   **Project Architecture:** I gained a deep understanding of the standard Python project layout and how configuration files like `pyproject.toml` orchestrate the development environment.
*   **FastAPI Ecosystem:** I mastered using Pydantic for request validation and how to leverage FastAPI's dependency injection for cleaner code.
*   **CI/CD Workflows:** I learned how to automate quality assurance using GitHub Actions, ensuring that every push meets linting and testing standards.

---

## 🚀 Future Roadmap: Scaling the Project

While this project serves as a robust proof-of-concept, the following features are planned for future iterations to make it production-ready:

1.  **Relational Database Integration:** Replace the local JSON persistence with **PostgreSQL** using **SQLAlchemy ORM**. This will allow for complex queries, better data integrity, and scalability.
2.  **Authentication & Authorization:** Implement **OAuth2 with JWT tokens** to secure the `POST`, `PUT`, and `DELETE` endpoints.
3.  **Containerization:** Add a `Dockerfile` and `docker-compose.yml` to ensure the API runs consistently across different deployment environments.
4.  **Async Database Drivers:** Transition to `asyncpg` to take full advantage of FastAPI’s asynchronous capabilities for high-concurrency performance.

---

## 📄 Project Structure

```text
📂 dog-breed-api/ (Root)
├── 📂 .github/workflows/
│   └── 📄 python-app.yml       # 🤖 GitHub Actions CI Configuration
├── 📂 tests/
│   └── 📄 test_dogs.py         # 📄 Unit tests 
├── 📂 .venv/                   # 🐍 Python Virtual Environment
├── 📄 dogs.json                # 🗄️ JSON database file
├── 📄 main.py                  # 🚀 FastAPI entry point & CRUD logic
├── 📄 README.md                # 📖 Project documentation
├── 📄 pyproject.toml           # 📦 Modern project configuration
├── 📄 commands.txt             # ⌨️ CLI Command reference
└── 📄 test_main.http           # ⚡ REST Client test file
```
