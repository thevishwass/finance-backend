from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database.db import Base, engine
from .api import users, records, dashboard


# Creates database table

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Dashboard Backend",
    description="Backend system for managing financial records with role-based access control and analytics.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(users.router, prefix="/api/v1")
app.include_router(records.router, prefix="/api/v1")
app.include_router(dashboard.router, prefix="/api/v1")


@app.get("/", tags=["System"])
def root():
    return {
        "message": "Finance Dashboard Backend API",
        "version": "1.0.0",
        "documentation": "/docs",
        "health_check": "/health"
    }


@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "ok",
        "service": "finance-dashboard-backend"
    }