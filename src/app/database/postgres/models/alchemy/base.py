from sqlalchemy import Column, Integer, MetaData
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    metadata = MetaData()


class TestModel(Base):
    __tablename__ = "test"

    table_id = Column(Integer, primary_key=True, autoincrement=True)
