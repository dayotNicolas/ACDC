import json
import datetime

from app import models
from database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

# Opening JSON file
with open('dataset/data.json') as json_file:
    data = json.load(json_file)

    for row in data:
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
