# coding: utf-8
__author__ = "Alison Mukoma"
__copyright__  = "DevsBranch"
__date__ = "14/11/2020"
"""
welcome to the python expert series compilation
The joys of live coding.

The code in here was initialized from a live pybootcamp coding session. 
But we feel ambitious to grow it into a fancy bookmarking application 
or better that we can then find useful  for keeping track of online content 
whilst on a path to sharpen our python expertize. 
Welcome aboard ship Nebuchadnezzar in the city of zion (^__^)
"""


from sqlalchemy import (
    create_engine, Column, Date,
    Integer, String, Date, ForeignKey, Text)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_path = '../models/orm_py.db'
db_engine = create_engine('sqlite:///{}'.format(db_path))

Base = declarative_base()

Session = sessionmaker(bind=db_engine)
my_session = Session()


class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(50), unique=True)
    password = Column('password', String(200))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<Object name: {self.username}>'

class UserDetails(Base):
    __tablename__ = 'user_details'

    id = Column(Integer, primary_key=True)
    cell = Column(String)
    address = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
    date = Column(Date)

    def __init__(self, cell, address, date):
        self.cell = cell
        self.address = address
        self.date = date

Base.metadata.create_all(db_engine)
