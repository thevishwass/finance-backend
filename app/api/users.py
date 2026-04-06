from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.db import SessionLocal
from ..database.models import User
from ..schemas.user import UserCreate
from ..middleware.role_guard import require_role

# router = APIRouter(prefix="/users")

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@router.post("/")
def create_user(user: UserCreate,
                db: Session = Depends(get_db),
                current=Depends(require_role(["admin"]))):

    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()

    return {"message": "User created"}