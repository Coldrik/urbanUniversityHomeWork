from fastapi import FastAPI, Path, Body, HTTPException, Request
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []

class User (BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/")
async def get_htmp(request: Request) -> HTMLResponse:

    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get(path="/user/{user_id}")
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post('/user/{username}/{age}')
async def create_user(user: User) -> str:
    user.id = len(users)
    users.append(user)
    return f"User {user.username} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def put_user(user_id: int,
                   username: str = Path(min_length=5, max_length=20, description='Enter username',
                                        example='UrbanUser'),
                   age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:

    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return f"The user {username} is registered"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"The user {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
