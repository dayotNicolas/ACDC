"""
* To install FastApi
-> pip install fastapi

* To install ASGI server
-> pip install "uvicorn[standard]"

* To install SQLAlchemy
-> pip install SQLAlchemy

* To install scrapy
-> pip install scrapy

* To run uvicorn server
-> uvicorn main:app --reload
    The command uvicorn main:app refers to:
       - main: the file main.py (the Python "module").
       - app: the object created inside of main.py with the line app = FastAPI().
       - --reload: make the server restart after code changes. Only do this for development.

* Access to generate doc
-> http://127.0.0.1:8000/docs.

* Package to install :
    - FastAPI
    - sqlalchemy
"""

from typing import Optional
from fastapi import FastAPI
import sqlalchemy
import jsonify

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
