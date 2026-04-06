# Finance Dashboard Backend

A backend system for managing financial records with role-based access control and dashboard analytics.

---

## Tech Stack

- FastAPI
- SQLAlchemy ORM
- SQLite

---

## Features

- User management with roles — viewer, analyst, admin
- Financial record CRUD operations
- Dashboard summary analytics
- Role-based access control via FastAPI dependencies
- Filtering by type, category, and date range with pagination

---

## Setup

```bash
git clone https://github.com/thevishwass/finance-backend
cd finance-dashboard-backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## API Documentation

FastAPI generates interactive API docs automatically.

```
http://localhost:8000/docs
```

---

## Role Permissions

| Role    | Permissions                                                |
|---------|------------------------------------------------------------|
| viewer  | View dashboard analytics                                   |
| analyst | View financial records, access dashboard analytics         |
| admin   | Manage users, create, update, and delete financial records |


# Made by Vishwas :)


