from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


# FastAPI - this class use to create a app
# Depends - tells fastapi run this function first and give the result
# HttpExecution - lets you return the proper error responses
# Session - just the type hint for "this is a database session"

import models
import schemas

from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine) #creates the table if they dont exist
# This runs once, at startup. It looks at every class that inherited from Base (your Item model) and creates the matching table in items.db if it doesn't already exist. If the table's already there from a previous run, this line does nothing — it's safe to run every time you start the app.

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# This is a pattern, not just a function. Here's what happens, in order, every single time any endpoint runs:

# db = SessionLocal() → opens a fresh session (your "notepad" from earlier)
# yield db → pauses here and hands db over to the endpoint function to use
# The endpoint runs completely (query, add, commit, whatever it does)
# Once the endpoint is done, execution comes back to this function, after the yield
# db.close() runs → the session is closed/cleaned up



# response_model=schemas.ItemResponse → whatever you return gets validated/shaped to match ItemResponse before being sent as JSON
# item: schemas.ItemCreate → FastAPI reads the incoming JSON body and validates it matches ItemCreate (so name and price must be there)
# item.model_dump() → converts the Pydantic object into a plain dict, e.g. {"name": "Laptop", "description": None, "price": 1000}
# models.Item(**item.model_dump()) → unpacks that dict into keyword arguments, creating a SQLAlchemy Item object: models.Item(name="Laptop", description=None, price=1000)
# db.add() → stage it
# db.commit() → actually save it (the only write to disk)
# db.refresh() → reload it, so it now has the auto-generated id
# return db_item → FastAPI converts this into JSON using ItemResponse (this is where from_attributes=True from schemas.py kicks in — it's reading from a SQLAlchemy object, not a dict)

# {} => this call path parameter
# parameters inside the function directly this is called 

@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
# For list of items return define response model as list
@app.get("/get-all", response_model=List[schemas.ItemResponse])
def get_all_item(skip : int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Item).offset(skip).limit(limit).all()

@app.get("/get-items/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int,db: Session = Depends(get_db)):
    return db.query(models.Item).filter(models.Item.id ==item_id).first()


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI Prasanth"}