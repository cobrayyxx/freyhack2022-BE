from psycopg2 import Timestamp
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)

class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    creator = Column(String, ForeignKey("users.username"))
    name = Column(String)
    latitude = Column(Integer)
    longitude = Column(Integer)
    location = Column(String)
    description = Column(String)
    contact = Column(String)
    num_participants = Column(Integer)
    # date_time = Column(Timestamp)

class Request(Base):
    __tablename__ = "request"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("event.id"))
    requester_id = Column(String, ForeignKey("users.username"))
    request_message = Column(String)
    accept = Column(Boolean)

class Enrolled(Base):
    __tablename__ ="enrolled"

    event_id = Column(Integer,ForeignKey("event.id"), primary_key=True)
    username = Column(String, ForeignKey("users.username"), primary_key=True)




    
    


