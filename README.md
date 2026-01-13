## Overview
This project is a RESTful Employee Management API built with FastAPI.
It supports CRUD operations, JWT authentication, pagination, filtering,
validation, and unit testing.

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- JWT
- Pytest

## Setup Instructions
1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Run server

## Authentication
POST /api/token
Use Bearer token for all secured endpoints

## API Endpoints
- POST /api/employees/
- GET /api/employees/
- GET /api/employees/{id}
- PUT /api/employees/{id}
- DELETE /api/employees/{id}

## Pagination & Filtering
- Page size: 10
- Filters: department, role

## Testing
Run:
python -m pytest
