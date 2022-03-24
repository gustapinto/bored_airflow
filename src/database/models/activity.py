from sqlalchemy import Column, Integer, String, SmallInteger, DECIMAL
from sqlalchemy.orm import declarative_base

from src.database.database import Base


class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    kind = Column(String(50), nullable=False)
    participants = Column(SmallInteger, nullable=False)
    price = Column(DECIMAL(2), nullable=False)
