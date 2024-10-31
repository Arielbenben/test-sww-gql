from sqlalchemy import Column, Integer,String, Float
from app.db.models import Base



class Country(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String)