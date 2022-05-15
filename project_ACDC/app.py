from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
import models
import schemas
from database import SessionLocal, engine
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from api_handler import *

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Use the string to create a jinja template
templates = Jinja2Templates(directory="templates")

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("accueil.html", {
        "request": request
    })


@app.get("/regions/", response_class=HTMLResponse)
async def regions(request: Request, db: Session = Depends(get_db)):
    regions = db.query(models.Region).all()

    return templates.TemplateResponse("region.html", {
        "request": request,
        "regions": regions
    })


@app.get("/hospitalisation/", response_class=HTMLResponse)
async def hospitalisation(request: Request, db: Session = Depends(get_db)):
    hospitalisations = []
    for u in db.query(models.HospitalisationAge).all():
        u.__dict__.pop('_sa_instance_state', None)
        hospitalisations.append(u.__dict__)
    return templates.TemplateResponse("hospitalisationAge.html", {
        "request": request,
        "hospitalisations": hospitalisations
    })


@app.get("/death/", response_class=HTMLResponse)
async def death(request: Request, db: Session = Depends(get_db)):
    deaths = []
    for u in db.query(models.DeathAgeRegion).all():
        u.__dict__.pop('_sa_instance_state', None)
        u.__dict__['date'] = u.__dict__['date'].strftime("%m/%d/%Y")
        deaths.append(u.__dict__)
    deaths.sort(key = lambda x:x['date'])
    return templates.TemplateResponse("deathAgeRegion.html", {
        "request": request,
        "deaths": deaths
    })


@app.get("/vaccinPercentage/", response_class=HTMLResponse)
async def vaccinPercentage(request: Request, db: Session = Depends(get_db)):
    vaccinPercentages = []
    for u in db.query(models.ProfessionalVaccinPercentageDepartment).all():
        u.__dict__.pop('_sa_instance_state', None)
        u.__dict__['date'] = u.__dict__['date'].strftime("%m/%d/%Y")
        vaccinPercentages.append(u.__dict__)
    return templates.TemplateResponse("professionalVaccinPercentageDepartment.html", {
        "request": request,
        "vaccinPercentages": vaccinPercentages
    })


@app.get("/vaccinationRate/", response_class=HTMLResponse)
async def vaccinationRate(request: Request, db: Session = Depends(get_db)):
    vaccinationRate = db.query(models.VaccinationRate).all()

    return templates.TemplateResponse("vaccinationRate.html", {
        "request": request,
        "vaccinationRats": vaccinationRate
    })


@app.get("/data_db/")
def put_data_in_db():
    middleware_deces_age()
    middleware_hospitalisation_age()
    middleware_professional_vaccin_percentage_department()
    middleware_vaccination_rate()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9856)
