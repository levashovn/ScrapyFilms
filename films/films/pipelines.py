# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from sqlalchemy.orm import sessionmaker
from .models import Movie, db_connect, create_movies_table


class KinopoiskPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_movies_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        movie = Movie(**item)

        try:
            session.add(movie)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

class ImdbPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_movies_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        movie = Movie(**item)

        try:
            session.add(movie)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
