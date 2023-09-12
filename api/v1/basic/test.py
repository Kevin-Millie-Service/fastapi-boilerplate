from typing import List, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.book.crud_book import crud_book
from api import deps
from schemas.book.book import Book

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}



@router.get("/book", response_model=Book)
def read_books(db: Session = Depends(deps.get_db)) -> Any:
    """
    Retrieve users.
    """
    book = crud_book.get_by_bookname(db, book_name='abc')
    return book
