from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import FastAPI, Path, Query, HTTPException, Depends, Response

from fastapi.security import OAuth2PasswordRequestForm
from enum import StrEnum
from demo_app.data import list_my_data
from pydantic import BaseModel, EmailStr
from typing import Annotated

from datetime import datetime, timedelta, timezone


app = FastAPI()

key="prasanth-secret"


fake_db_user = {
    # "pr@gmail.com" : {
    #     "name" : "prasanth", 
    #     "email" : "pr@gmail.com",
    #     "password" : "304830843843",
    #     "disabled" : False
    # }
}

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

class Users(BaseModel):
    name : str
    email : EmailStr
    disabled: bool

class UserInDB(Users):
    password : str

class LoginUser(BaseModel):
    email : EmailStr
    password : str


class UserCreate(BaseModel):
    name : str
    email : EmailStr
    password : str

def get_user(user_db, email: str):
    if email in user_db:
        user_dict = user_db[email]
        return UserInDB(**user_dict)


def get_current_user_active(email: EmailStr):
    val = get_user(fake_db_user, email)
    if val.disabled == False:
        return {
            "user" : val,
            "available": True
        }
    return {
        "available": False,
        "user" : {}
    }

password_hash = PasswordHash.recommended()


def getPasswordHash(password):
    return password_hash.hash(password)


def validatePassword(plain_password: str, hashed_password: str):
     return password_hash.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, "prasanth-secret", algorithm="HS256")


@app.post('/signup', response_model=Users)
async def usersignup(user: UserCreate):
    print(fake_db_user)
    if user.email in fake_db_user:
        raise  HTTPException(
            status_code=400,
            detail='User Exist'
        )
    hash_password = getPasswordHash(user.password)

    fake_db_user[user.email] = {
        "name" : user.name,
        "email" : user.email,
        "disabled" :  False,
        "password" : hash_password
    }


    return Users(**fake_db_user[user.email])


@app.post('/login')
async def userLogin(user: Annotated[OAuth2PasswordRequestForm, Depends()], response : Response ):

    check_user_exist = get_current_user_active(user.username)

    if  not check_user_exist["available"] or not validatePassword(user.password, check_user_exist["user"].password):
        return HTTPException(
            status_code=404
        )

    response.set_cookie(
        key="accesstoken",
        
    )
    
    return {
        "access_token":"test"
    }
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



#Annotated

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


@app.get('/user-data/{id}')
async def data_get(id: Annotated[str,Path(title="The ID of the item to get")]): 
    return id





