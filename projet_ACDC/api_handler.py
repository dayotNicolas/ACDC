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
        print(data)
        for Column in data:
            db_record = models.DeathAgeRegion(
                region_id=Column["reg"],
                cl_age90=Column["cl_age90"],
                deaths_covid=Column["Dc_Elec_Covid_cum"],
                date=Column["jour"]
            )
            db.add(db_record)
        db.commit()

    db.close()
