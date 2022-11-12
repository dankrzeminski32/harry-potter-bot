from src.models.db import Base
from sqlalchemy import Column, Integer, String


class Wizard(Base):
    __tablename__ = "wizards"
    id = Column(Integer, primary_key=True)
    house_id = Column(Integer)
    pet_id = Column(Integer)
    wand_id = Column(Integer)
    prefix = Column(String)
    level = Column(Integer)
