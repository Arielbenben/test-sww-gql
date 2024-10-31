from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker
from app.settings.config import DB_URL
from app.db.models import Base



engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)




