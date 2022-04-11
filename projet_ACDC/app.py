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

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

templates = Jinja2Templates(directory="templates")


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/departments/", response_model=List[schemas.Departments])
def show_records(db: Session = Depends(get_db)):
    departments = db.query(models.Departments).all()
    return departments


@app.get("/plots/", response_class=HTMLResponse)
def read_notes(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    departments = db.query(models.Departments).all()
    print(departments)
    return templates.TemplateResponse("plots.html", {
        "request": request,
        "departments": departments
    })


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9856)
