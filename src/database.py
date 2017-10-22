import sqlite3
from src.user import User
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, create_engine
import sqlalchemy.types as types
from sqlalchemy.orm import mapper, sessionmaker, relationship
#database class
class Database():
    def __init__(self, connection_string='sqlite:///APIlesToORMgesDB.sqlite3'):
        self.sql_file = connection_string
        self.engine = self._get_connection()
        self.metadata = MetaData(bind=self.engine)
    def _map_users(self):
        users = Table('Users', self.metadata,\
                      Column('user_id', Integer, primary_key=True),
                      Column('first_name', String),
                      Column('last_name', String),
                      Column('email_address', String),
                      Column('password', String))
        users.create(self.engine, checkfirst=True)
        mapper(User, users)
        return users
    def _get_connection(self):
        engine = create_engine(self.sql_file)
        return engine
    def _get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session