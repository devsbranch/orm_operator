# EXPERT PYTHON SERIES
# classes - intensive
# interacting python - SQL
# python for everything - classes
# packages/modules - thousands of built in python modules,
# 3rd party modules/libraries - install using, pip3 install package-name
# alias pip=pip3

# sqlite3 = MSSQL,  mysql, psql, mdb, oracle
# ORM - object relational model

# 3rd party library - `pip3 install sqlalchemy`

# db -> users.py
# mechanics -> controllers/app/freestyle.py
# UI -> templates -> flask

# users.py - db - OOP classes + methods + functions


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






























