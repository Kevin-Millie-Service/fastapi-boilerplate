from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    book_seq: Optional[int] = None
    book_name: str = None
    full_name: Optional[str] = None

    class Config:
        from_attributes = True


# Additional properties to return via API
class Book(BookBase):
    pass
