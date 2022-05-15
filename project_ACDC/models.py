import json

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.types import Date
from database import Base


class Region(Base):
    __tablename__ = "Region"

    id = Column(Integer, primary_key=True, index=True)
    region_number = Column(String(10))
    name = Column(String(255), nullable=False)


class HospitalisationAge(Base):
    __tablename__ = "hospitalisationAge"

    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("Region.id"), index=True)
    week = Column(String(255))
    cl_age90 = Column(Integer)
    new_admission_hospitals = Column(Integer)


class DeathAgeRegion(Base):
    __tablename__ = "deathAgeRegion"

    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("Region.id"), index=True)
    cl_age90 = Column(Integer)
    deaths_covid = Column(Integer)
    date = Column(Date)


class ProfessionalVaccinPercentageDepartment(Base):
    __tablename__ = "ProfessionalVaccinPercentageDepartment"

    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("Region.id"), index=True)
    date = Column(Date)
    dose1 = Column(Float)
    dose_completed = Column(Float)
    dose_rappel = Column(Float)


class VaccinationRate(Base):
    __tablename__ = "VaccinationRate"

    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("Region.id"), index=True)
    vaccin_number = Column(Integer)
    date = Column(Date)
    n_dose1 = Column(Integer)
    n_dose2 = Column(Integer)
    n_dose3 = Column(Integer)
    n_dose4 = Column(Integer)
    n_rappel = Column(Integer)
    n_cum_dose1 = Column(Integer)
    n_cum_dose2 = Column(Integer)
    n_cum_dose3 = Column(Integer)
    n_cum_dose4 = Column(Integer)
    n_cum_rappel = Column(Integer)
