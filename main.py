from fastapi import FastAPI
from db.user_db import database_users
from fastapi import HTTPException
from db.user_db import UserInDB
app = FastAPI()


@app.get("/")
async def root():
   return {"menssage":"Hola FastAPI"}

@app.get("/users")
async def users():
   return {"menssage":database_users}

@app.get("/users/{username}")
async def get_use_by_usernames(username : str):
   if username in database_users:
       return {"menssage":database_users[username]}
   raise HTTPException(status_code = 404, detail = "El usaurio no existe")

@app.post("/users/")
async def create_user(user : UserInDB):
   database_users[user.username] = user
   return user

@app.delete("/users/")
async def delete_user(user : UserInDB):
   del database_users[user.username]
   return user

@app.put("/users/")
async def create_user(user : UserInDB):
   database_users[user.username] = user
   return user