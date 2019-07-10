import logging
from sqlalchemy import create_engine, Column, Integer, String, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.types import ARRAY
from . import settings

DeclarativeBase = declarative_base()


def db_connect():
    db_url = URL(**settings.DATABASE)
    logging.info("Creating an SQLAlchemy engine at URL '{db_url}'".format(db_url=db_url))
    return create_engine(db_url)


def create_movies_table(engine):
    DeclarativeBase.metadata.create_all(engine)




class Movie(DeclarativeBase):
    __tablename__ = "MovieDict"
    movie_id = Column(String, primary_key=True)
    title = Column('title', String)
    director = Column('director', String)
    genre = Column('genre', String)
    recommended = Column('recommended', ARRAY(String))
    date = Column('date', DATE)
    country = Column('country', String)
    platform = Column('platform', String)
    cast = Column('cast', ARRAY(String))
    synopsis = Column('synopsis', String)
    duration = Column('duration', String)


