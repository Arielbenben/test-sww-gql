from sqlalchemy import Column, Integer, ForeignKey,String
from sqlalchemy.orm import relationship
from app.db.models import Base



class Target(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    target_industry = Column(String)
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    target_priority = Column(Integer)

    mission = relationship('Mission', back_populates='target', lazy="immediate")
    city = relationship('City', lazy="immediate")
    target_type = relationship('TargetType', lazy="immediate")