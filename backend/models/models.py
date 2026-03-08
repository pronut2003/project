from sqlalchemy import Column, Integer, String
from database.db import Base

class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    firstname = Column(String(50), nullable = False)
    lastname = Column(String(50), nullable = False)
    phone   = Column(String(50), nullable = False)
    emailid = Column(String(50), nullable = False, unique = True)