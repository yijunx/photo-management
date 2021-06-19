from sqlalchemy import Column, String, DateTime

from .base import Base


class Photo(Base):
    __tablename__ = "photos"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # no user-management for now
    # created_by = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
