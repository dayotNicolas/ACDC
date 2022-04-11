from pydantic import BaseModel
import datetime


class Region(BaseModel):
    id: int
    name: str
    region_number: str

    class Config:
        orm_mode = True


class HospitalisationAge(BaseModel):
    id: int
    region_id: int
    week: str
    cl_age90: int
    new_admission_hospitals: int

    class Config:
        orm_mode = True


class DeathAgeRegion(BaseModel):
    id: int
    region_id: int
    cl_age90: int
    deaths_covid: int
    date: datetime.date

    class Config:
        orm_mode = True


class ProfessionalVaccinPercentageDepartment(BaseModel):
    id: int
    region_id: int
    date: datetime.date
    dose1: float
    dose_completed: float
    dose_rappel: float

    class Config:
        orm_mode = True


class VaccinationRate(BaseModel):
    id: int
    region_id: int
    vaccin_number: int
    date: datetime.date
    n_dose1: int
    n_dose2: int
    n_dose3: int
    n_dose4: int
    n_rappel: int
    n_cum_dose1: int
    n_cum_dose2: int
    n_cum_dose3: int
    n_cum_dose4: int
    n_cum_rappel: int

    class Config:
        orm_mode = True
