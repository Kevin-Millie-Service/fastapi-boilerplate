from typing import Any, Dict, Optional, Union

from crud.base.base import CRUDBase
from models.book.book import Book

from sqlalchemy.orm import Session

class CRUDBook(CRUDBase[Book, None, None]):
    def get_by_bookname(self, db: Session, *, book_name: str) -> Optional[Book]:
        return db.query(Book).filter(Book.book_name == book_name).first()


crud_book = CRUDBook(Book)