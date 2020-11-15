# coding: utf-8
__author__ = "Alison Mukoma"
__copyright__  = "DevsBranch"
__date__ = "14/11/2020"
"""
Welcome to the python expert series compilation
The joys of live coding.

The code in here was initialized from a live pybootcamp coding session. 
But we feel ambitious to grow it into a fancy bookmarking application 
or better that we can then find useful  for keeping track of online content 
whilst on a path to sharpen our python expertize. 
Once more welcome aboard ship Nebuchadnezzar in the city of zion (^__^).
"""

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_path = '../models/orm_py.db'
db_engine = create_engine('sqlite:///{}'.format(db_path))

Base = declarative_base()

Session = sessionmaker(bind=db_engine)
my_session = Session()