from database import BaseClass
from sqlalchemy import Column, Integer, String

class Student(BaseClass):
   
    __tablename__ = "student_details"
    

    id = Column(Integer,primary_key=True,index=True)
    student_name = Column(String, nullable = False)
    student_email = Column(String, unique=True, nullable=False)
    student_password = Column(String)
    