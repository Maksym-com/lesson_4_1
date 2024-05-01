from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
def create_all():
    """create all tables if they don't exist"""
    Base.metadata.create_all(engine)

def drop_all():
    """"drop all tables if they exist"""
    Base.metadata.drop_all(engine)
