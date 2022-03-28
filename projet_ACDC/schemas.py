from pydantic import BaseModel


class Departments(BaseModel):
    id: int
    name: str
    department_number: int
    cases: int
    deaths: int
    icu_occupation: int
    vaccination_rate: int
    positivity_rate: int

    class Config:
        orm_mode = True