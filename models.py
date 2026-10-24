from sqlalchemy import Column, Integer, String, Date
from database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, unique=True, index=True)  # your unique ID like "STU001"
    name = Column(String, nullable=False)
    dob = Column(Date)
    email = Column(String)
    phone = Column(String)
    course = Column(String, nullable=True)
    address = Column(String, nullable=True)