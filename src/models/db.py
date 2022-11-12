from sqlalchemy.orm import Session
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URI

Base = declarative_base()

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def recreateDB():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


recreateDB()
