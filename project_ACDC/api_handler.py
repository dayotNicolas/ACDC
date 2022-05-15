import csv
import json
import datetime
from app import models
from database import SessionLocal, engine
import pandas as pd


def create_database():
    db = SessionLocal()

    models.Base.metadata.create_all(bind=engine)
    with open("datasets/departements-region.csv", "r") as f:
        csv_reader = csv.DictReader(f)
    for Column in csv_reader:
        db_record = models.Region(
            id=Column["department_number"],
            region_number=Column["department_number"],
            name=Column["name"]
        )
        db.add(db_record)
    db.commit()

    db.close()


def middleware_deces_age():
    pass
    db = SessionLocal()

    models.Base.metadata.create_all(bind=engine)
    with open('datas/JSON/deces_age_region.json') as json_file:
        data = json.load(json_file)
        for Column in data.items():
            print(Column[0], type(int(Column[1]['reg'])))
            db_record = models.DeathAgeRegion(
                region_id=int(Column[1]["reg"]),
                cl_age90=int(Column[1]["cl_age90"]),
                deaths_covid=int(Column[1]["Dc_Elec_Covid_cum"]),
                date=pd.to_datetime(Column[1]["jour"])
            )
            db.add(db_record)
        db.commit()

    db.close()


def middleware_hospitalisation_age():
    pass
    db = SessionLocal()

    models.Base.metadata.create_all(bind=engine)
    with open('datas/JSON/hospitalisation_age.json') as json_file:
        data = json.load(json_file)
        for Column in data.items():
            print(Column[0], type(int(Column[1]['reg'])))
            db_record = models.HospitalisationAge(
                region_id=int(Column[1]["reg"]),
                week=str(Column[1]["Semaine"]),
                cl_age90=int(Column[1]["cl_age90"]),
                new_admission_hospitals=int(Column[1]["NewAdmHospit"])
            )
            db.add(db_record)
        db.commit()

    db.close()


def middleware_professional_vaccin_percentage_department():
    pass
    db = SessionLocal()

    models.Base.metadata.create_all(bind=engine)
    with open('datas/JSON/vaccin_pro_poucentage_dep.json') as json_file:
        data = json.load(json_file)
        for Column in data.items():
            print(Column[0], type(int(Column[1]['dep'])))
            db_record = models.ProfessionalVaccinPercentageDepartment(
                region_id=int(Column[1]["dep"]),
                date=pd.to_datetime(Column[1]["jour"]),
                dose1=float(Column[1]["pro_couv_dose1"]),
                dose_completed=float(Column[1]["pro_couv_complet"]),
                dose_rappel=float(Column[1]["pro_couv_rappel"])
            )
            db.add(db_record)
        db.commit()

    db.close()

'''
def middleware_vaccination_rate():
    pass
    db = SessionLocal()

    models.Base.metadata.create_all(bind=engine)
    with open('datas/JSON/vaccin_cage_date.json') as json_file:
        data = json.load(json_file)
        for Column in data.items():
            print(Column[0], type(int(Column[1]['dep'])))
            db_record = models.VaccinationRate(
                region_id=int(Column[1]["dep"]),
                vaccin_number=int(Column[1]["vaccin"]),
                date=pd.to_datetime(Column[1]["jour"]),
                n_dose1=int(Column[1]["n_dose1"]),
                n_dose2=int(Column[1]["n_dose2"]),
                n_dose3=int(Column[1]["n_dose3"]),
                n_dose4=int(Column[1]["n_dose4"]),
                n_rappel=int(Column[1]["n_rappel"]),
                n_cum_dose1=int(Column[1]["n_cum_dose1"]),
                n_cum_dose2=int(Column[1]["n_cum_dose2"]),
                n_cum_dose3=int(Column[1]["n_cum_dose3"]),
                n_cum_dose4=int(Column[1]["n_cum_dose4"]),
                n_cum_rappel=int(Column[1]["n_cum_rappel"]),

            )
            db.add(db_record)
        db.commit()

    db.close()
'''