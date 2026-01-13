# Employee Management API

A secure RESTful API built using FastAPI to manage employees with CRUD operations, JWT authentication, pagination, filtering, and tests.

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Auth
POST /api/token → Bearer Token

## Run Tests
```bash
pytest
```
