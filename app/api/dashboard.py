from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.db import get_db
from ..database.models import Record
from ..services.dashboard_service import calculate_summary
from ..middleware.role_guard import require_role

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard Analytics"]
)


@router.get("/summary")
def summary(
    db: Session = Depends(get_db),
    current=Depends(require_role(["admin", "analyst", "viewer"]))
):

    records = db.query(Record).all()

    return calculate_summary(records)


@router.get("/category-breakdown")
def category_breakdown(
    db: Session = Depends(get_db),
    current=Depends(require_role(["admin", "analyst"]))
):

    records = db.query(Record).all()

    totals = {}

    for r in records:
        totals[r.category] = totals.get(r.category, 0) + r.amount

    return totals


@router.get("/recent")
def recent_records(
    limit: int = 5,
    db: Session = Depends(get_db),
    current=Depends(require_role(["admin", "analyst"]))
):

    records = (
        db.query(Record)
        .order_by(Record.date.desc())
        .limit(limit)
        .all()
    )

    return records

