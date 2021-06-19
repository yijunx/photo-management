from typing import List, Optional
from pydantic import BaseModel


class QueryPagination(BaseModel):
    page: Optional[int] = 1
    size: Optional[int] = 5


class ResponsePagination(BaseModel):
    total: int
    page_size: int
    current_page: int
    total_pages: int
