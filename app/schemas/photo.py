from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .pagination import QueryPagination, ResponsePagination


class PhotoCreate(BaseModel):
    title: str
    description: Optional[str]


class Photo(PhotoCreate):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


class PhotoPatch(PhotoCreate):
    pass


class PhotoQuery(QueryPagination):
    pass


class PhotoWithPagination(BaseModel):
    data: List[Photo]
    paging: ResponsePagination
