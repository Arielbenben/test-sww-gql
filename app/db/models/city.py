from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.db.models import Base



class City(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String)
    country_id = Column(Integer, ForeignKey('countries.country_id'))
    latitude = Column(Float)
    longitude = Column(Float)

