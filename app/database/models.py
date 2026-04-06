from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, index=True, nullable=False)

    password = Column(String(255), nullable=False)

    role = Column(String(20), nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship
    records = relationship(
        "Record",
        back_populates="creator",
        cascade="all, delete-orphan"
    )


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Float, nullable=False)

    type = Column(String(20), nullable=False)

    category = Column(String(100), nullable=False)

    date = Column(Date, nullable=False)

    notes = Column(String(255))

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    created_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    # Relationship
    creator = relationship(
        "User",
        back_populates="records"
    )