#!/usr/bin/python3
"""Module for database storage"""
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all objects"""
        classes = (User, State, City, Amenity, Place, Review)
        objs = {}

        if cls is None:
            for item in classes:
                query = self.__session.query(item)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.name__, obj.id)
                    objs[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objs[obj_key] = obj
        return objs

    def new(self, obj):
        """Adds new object"""
        self.__session.add(obj)

    def save(self):
        """Save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables and current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Calls remove() method on the private session attribute"""
        self.__session.remove()
