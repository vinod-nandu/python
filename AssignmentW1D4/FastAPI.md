# FastAPI Quick-Start Guide

This guide walks you through setting up a clean environment, installing **FastAPI**, writing a basic web API, and launching it with a server.

---

## 1. Setup Your Environment

To avoid dependency conflicts, it is best practice to create an isolated environment for your project.

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows (Command Prompt):
venv\Scripts\activate
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
```

---

## 2. Install Dependencies

FastAPI requires an ASGI server like **Uvicorn** to run your code. Install both packages together:

```bash
pip install fastapi uvicorn
```

---

## 3. Create the API Code (`main.py`)

Create a file named `main.py` and paste the following Python code. This sets up standard `GET` and `POST` routes while utilizing explicit REST status codes.

```python
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional

# Initialize the FastAPI instance
app = FastAPI(
    title="My First Web API",
    description="A basic FastAPI example with structural status codes.",
    version="1.0.0"
)

# Define a Pydantic model for request data validation
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

# 1. Root Endpoint (Universal Status Code 200)
@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {"message": "Welcome to my FastAPI application!"}

# 2. Path Parameter Endpoint
@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "query_param": q,
        "status": "Success"
    }

# 3. Create Endpoint (Explicit Status Code 201 Created)
@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return {
        "message": "Item successfully registered",
        "data": item
    }
```

---

## 4. Run the Server

Launch your development server locally using **Uvicorn**:

```bash
uvicorn main:app --reload
```

*   `main`: Refers to your Python file name (`main.py`).
*   `app`: Refers to the `app = FastAPI()` object inside that file.
*   `--reload`: Automatically restarts the server whenever you save code changes.

---

## 5. View it in Your Browser

Open your browser and navigate to the following addresses to see your API in action:

*   **Live API Response:** Go to `http://127.0.0.1:8000/` to see the JSON root response.
*   **Interactive Swagger Documentation:** Go to `http://127.0.0.1:8000/docs`. This automatically generated interface allows you to test your endpoints directly from your browser!
*   **Alternative ReDoc Documentation:** Go to `http://127.0.0.1:8000/redoc`.
