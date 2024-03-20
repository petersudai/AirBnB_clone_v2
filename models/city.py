#!/usr/bin/python3
""" City Module for HBNB project """
import sys
sys.path.append('/AirBnB_clone')
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states,id'), nullable=False)
    places = relationship('Place', cascade='all, delete, delete-orphan',
                          backref='cities')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
