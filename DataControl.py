import sqlite3
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

MyBase = declarative_base()


class City(MyBase):
    __tablename__ = "city"
    code = Column(Integer, primary_key=True)
    name = Column(VARCHAR(10))

    def __repr__(self):
        return "[City(name='{1}', code='{0}')]".format(self.code, self.name)


engine = create_engine('sqlite:///data.db')
MyBase.metadata.create_all(engine,checkfirst=True)