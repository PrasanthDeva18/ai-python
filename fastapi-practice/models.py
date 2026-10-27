from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Integer)
    discount = Column(Integer)


# Attributes in column - Type - Integer, String, Float, Boolean
# primary_key = True
# index = True
# nullable = True
# default = True based on type
# ForeignKey("tablename")
# DateTime
# Unique = True
# Text = no length limit
# relationship("Booking", back_populates="user") - Lets you navigate between linked tables in Python
class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    studentName = Column(String, index=True)
    studentAdd = Column(String, nullable=True)
    email = Column(String, nullable=True)

