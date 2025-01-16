from fastapi import FastAPI, HTTPException, Path, Request
from typing import List
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated

# python -m uvicorn module_16_5:app

app = FastAPI()

templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []


class UserCreate(BaseModel):
    username: str = Field(..., min_length=5,
                          max_length=20,
                          description="Enter Username", )
    age: int = Field(..., ge=18,
                     description="Enter age", )


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users, })


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def user_page(request: Request, user_id: Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/user/{username}/{age}", response_model=User)
async def post_user(user: User):
    new_id = max((u.id for u in users), default=0) + 1
    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: int, user: User):
    for u in users:
        if u.id == user_id:
            u.username = user.username
            u.age = user.age
            return u
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    for i, u in enumerate(users):
        if u.id == user_id:
            del_user = users[i]
            del users[i]
            return del_user
    raise HTTPException(status_code=404, detail="User was not found")
