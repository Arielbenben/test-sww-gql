from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker
from app.settings.config import DB_URL
from app.db.models import Base



engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True, autoincrement=True)


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)