#!/usr/bin/python3
""" Place Module for HBNB project """
import sys
sys.path.append('/AirBnB_clone')
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id',),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable = True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref='places_amenities', viewonly=False,)

    else:
        city_id = ""
        user_id = ""
        name = ""
        decription = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
