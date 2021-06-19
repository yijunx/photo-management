from app.schemas.pagination import ResponsePagination
from app.schemas.photo import Photo, PhotoCreate, PhotoPatch, PhotoWithPagination
from app.db import models
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime, timezone
from typing import Optional


def create(db: Session, item_create: PhotoCreate) -> models.Photo:
    item_id = str(uuid4())
    db_item = models.Photo(
        id=item_id,
        title=item_create.title,
        description=item_create.description,
        created_at=datetime.now(timezone.utc),
    )
    db.add(db_item)
    return db_item


def get_all(
    db: Session, page: Optional[int], size: Optional[int]
) -> PhotoWithPagination:
    query = db.query(models.Photo)

    # pagination
    total = query.count()
    limit = size or total
    offset = (page - 1) * limit if page else 0
    current_page = page or 1
    total_pages = -(-total // size) if size else 1

    db_items = (
        query.order_by(models.Photo.created_at.desc()).limit(limit).offset(offset)
    )

    data = [Photo.from_orm(x) for x in db_items]
    paging = ResponsePagination(
        total=total,
        total_pages=total_pages,
        current_page=current_page,
        page_size=len(data),
    )
    return PhotoWithPagination(data=data, paging=paging)


def get(db: Session, item_id: str) -> Photo:
    db_item = db.query(models.Photo).filter(models.Photo.id == item_id).first()
    if not db_item:
        raise Exception("photo id is not there")
    return db_item


def patch(db: Session, item_id: str, item_patch: PhotoPatch):
    db_item = get(db=db, item_id=item_id)
    db_item.title = item_patch.title or db_item.title
    db_item.description = item_patch.description or db_item.description
    return db_item


def delete(db: Session, item_id: str):
    db_item = get(db=db, item_id=item_id)
    db.delete(db_item)
