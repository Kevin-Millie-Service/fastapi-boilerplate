from sqlalchemy import Column, Integer, String

from db.base_class import Base


class Book(Base):
    book_seq = Column(Integer, primary_key=True, index=True)
    book_name = Column(String, comment='책 이름')

    __tablename__ = 'book_copy'

