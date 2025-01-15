from fastapi import FastAPI, Path
from typing import Annotated

# python -m uvicorn module_16_3:app

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_all_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_new_user(username: Annotated[str, Path(min_length=3,
                                                        max_length=20,
                                                        description="Enter Username",
                                                        example="DenisStudent")],
                          age: Annotated[int, Path(ge=18,
                                                   description="Enter age",
                                                   example="24")]):
    new_id = str(int(max(users, key=int)) + 1)
    new_info = f'Имя: {username}, возраст: {age}'
    users[new_id] = new_info
    return f'User {new_id} is registered'


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[str, Path(min_length=1,
                                                   description="Enter User ID",
                                                   example="1")],
                      username: Annotated[str, Path(min_length=3,
                                                    max_length=20,
                                                    description="Enter Username",
                                                    example="DenisStudent")],
                      age: Annotated[int, Path(ge=18,
                                               description="Enter age",
                                               example="24")]):
    for id, _ in users.items():
        if id == user_id:
            users[id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[str, Path(min_length=1,
                                                   description="Enter User ID",
                                                   example="1")]):
    users.pop(user_id)
    return f'The user {user_id} is deleted'
