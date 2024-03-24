#!/usr/bin/python3
"""City Module"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class"""
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
