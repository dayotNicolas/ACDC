import csv
import datetime

from app import models
from database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

with open("[LIEN DU CSV].csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        db_record = models.Departments(
            id=row["id"],
            name=row["name"],
            department_number=row['department_number'],
            cases=row["cases"],
            deaths=row["deaths"],
            icu_occupation=row['icu_occupation'],
            vaccination_rate=row['vaccination_rate'],
            positivity_rate=row['positivity_rate']
        )
        db.add(db_record)

    db.commit()

db.close()
