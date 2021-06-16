from pydantic import BaseModel
from typing import Optional


class Photo(BaseModel):
    url: str
    title: str
    description: Optional[str]
