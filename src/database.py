import sqlite3
from src.user import User
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, create_engine
import sqlalchemy.types as types
from sqlalchemy.orm import mapper, sessionmaker, relationship
METADATA = MetaData()

#database class
#sets the sql file, user, and engine
class Database():
    def __init__(self, connection_string='sqlite:///APIlesToORMgesDB.sqlite3'):
        self.sql_file = connection_string
        self.users = self._map_users()
        self.engine = self._get_connection()
        METADATA.create_all(self.engine)

    #map_users function that creates Table MetaData from Table then mapped to the Users class
    def _map_users(self):
        users = Table('Users', METADATA,
                      Column('user_id', Integer, primary_key=True),
                      Column('first_name', String),
                      Column('last_name', String),
                      Column('email_address', String),
                      Column('password', String))
        mapper(User, users)
        return users
    #Gets the connection with the sql file
    def _get_connection(self):
        engine = create_engine(self.sql_file)
        return engine
    #gets a session for the ORM
    def _get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()
    #adds a user to the database
    def add_user(self, user):
        session = self._get_session()
        session.add(user)
        session.commit()