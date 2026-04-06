# Finance Dashboard Backend

> A robust backend system for managing financial records with role-based access control and dashboard analytics.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **FastAPI** | High-performance async web framework |
| **SQLAlchemy ORM** | Database abstraction & query building |
| **SQLite** | Lightweight relational database |

---

## Features

- **User Management** — Create and manage users with scoped roles
- **Financial Record CRUD** — Full create, read, update, and delete operations
- **Dashboard Analytics** — Summary insights across financial data
- **Role-Based Access Control** — Enforced via FastAPI dependency injection
- **Advanced Filtering** — Filter by type, category, and date range with pagination

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/thevishwas/finance-backend

# Navigate to the project directory
cd finance-dashboard-backend

# Install dependencies
pip install -r requirements.txt

# Start the development server
uvicorn app.main:app --reload
```

---

## API Documentation

FastAPI auto-generates interactive API docs. Once the server is running, visit:

```
http://localhost:8000/docs
```

---

## Role Permissions

| Role | Permissions |
|---|---|
| `viewer` | View dashboard analytics |
| `analyst` | View financial records · Access dashboard analytics |
| `admin` | Manage users · Create, update & delete financial records |

---

## Project Structure

```
finance-dashboard-backend/
├── app/
│   ├── main.py          # Application entry point
│   ├── models/          # SQLAlchemy models
│   ├── routes/          # API route handlers
│   ├── dependencies/    # RBAC & auth dependencies
│   └── schemas/         # Pydantic request/response schemas
├── requirements.txt
└── README.md
```

---

<div align="center">

Made by **Vishwas**

</div>
