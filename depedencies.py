from database import databd
from sqlalchemy.orm import sessionmaker, Session


def operating_session():
    try:
        Session = sessionmaker(bind=databd.db)

        session = Session()

        yield session
    
    finally:
        session.close()
