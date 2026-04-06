from pydantic import BaseModel
from datetime import date
from typing import Optional

class RecordCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: Optional[str]


class RecordResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: date