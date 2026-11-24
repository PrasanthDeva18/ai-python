from fastapi import FastAPI
from enum import StrEnum
from demo_app.data import list_my_data
from pydantic import BaseModel

app = FastAPI()


class ModelName(StrEnum):
    prasanth = "prasanth"
    deva = "deva"
    vennila = "vennila"


class Items(BaseModel):
    name : str
    roll_no: int
    desc : str | None = None
    tax : float | None = None
    isWorking : bool



@app.post('/create')
async def createItems(items: Items):
    items_dict = items.model_dump() #convert into pure dict

    return items

#query params, body, path
@app.put("/update/{update_id}")
async def updateItems(items: Items, update_id: int, for_val:str | None = None):
    
    return {
        "return" : items,
        "upadate_id" : update_id,
        "query_val" : for_val
    }

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Path Parameters
@app.get("/details/{details}")
async def read_detail(details: int):
    return {details}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: ModelName):

    if user_id is ModelName.prasanth:
        return {"user_id": user_id}
    if user_id.value == "deva":
        return {"user_id": user_id, "message": "this message for deva"}

#Query parameter 
@app.get('/data/')
async def get_data(skip:int, limit:int = 10):
    return list_my_data[skip: skip+limit]




