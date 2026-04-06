from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import date

from ..database.db import get_db
from ..database.models import Record
from ..schemas.record import RecordCreate
from ..middleware.role_guard import require_role

router = APIRouter(
    prefix="/records",
    tags=["Financial Records"]
)


@router.post("/")
def create_record(
    record: RecordCreate,
    db: Session = Depends(get_db),
    current=Depends(require_role(["admin"]))
):

    db_record = Record(
        **record.dict(),
        created_by=current.id
    )

    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return db_record


@router.get("/")
def get_records(
    type: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
    current=Depends(require_role(["admin", "analyst"]))
):

    query = db.query(Record)

    if type:
        query = query.filter(Record.type == type)

    if category:
        query = query.filter(Record.category == category)

    if start_date:
        query = query.filter(Record.date >= start_date)

    if end_date:
        query = query.filter(Record.date <= end_date)

    total = query.count()

    records = query.offset(skip).limit(limit).all()

    return {
        "data": records,
        "pagination": {
            "total_records": total,
            "skip": skip,
            "limit": limit,
            "returned": len(records)
        }
    }


@router.delete("/{record_id}")
def delete_record(
    record_id: int,
    db: Session = Depends(get_db),
    current=Depends(require_role(["admin"]))
):

    record = db.query(Record).filter(Record.id == record_id).first()

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Record not found"
        )

    db.delete(record)
    db.commit()

    return {"message": "Record deleted"}


