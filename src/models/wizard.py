from models.db import Base
from sqlalchemy import Column, Integer, String, Date, BigInteger, Boolean, extract


class Wizard(Base):
    id = Column(Integer, primary_key=True)
    house_id = Column(Integer)
    pet_id = Column(Integer)
    wand_id = Column(Integer)
    prefix = Column(String)
    level = Column(Integer)
