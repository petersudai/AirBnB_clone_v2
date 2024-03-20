#!/usr/bin/python3
"""Module for database storage"""
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """This class manages database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all objects"""
        from models.stae import State
        from models.city import City
        if cls is None:
            objs = self.__session.query(State).all() + \
                self.__session.query(City).all()

        else:
            objs = self.__session.query(cls).all()
        return {'{}.{}'.format(type(obj).__name, obj.id): obj
                for obj in objs}

    def new(self, obj):
        """Adds new object"""
        self.__session.add(obj)

    def save(self):
        """Save changes"""
