from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from database import Base


class Departments(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Date)
    department_number = Column(String(255), index=True)
    cases = Column(Integer)
    deaths = Column(Integer)
    icu_occupation = Column(Integer)
    vaccination_rate = Column(Integer)
    positivity_rate = Column(Integer)


