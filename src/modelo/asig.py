from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.modelo.declarative_base import Base


class Asignatura(Base):
    __tablename__ = 'asignatura'
    id = Column(Integer(), primary_key=True)
    nombasig = Column(String(55), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.nombasig