from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel, Field

# python -m uvicorn module_16_4:app

app = FastAPI()


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


@app.get("/users", response_model=List[User])
async def get_all_users():
    return users


@app.post("/user/{username}/{age}", response_model=User)
async def create_new_user(user: User):
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
