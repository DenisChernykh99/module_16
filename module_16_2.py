from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def main_page():
    """
     Главная страница
     """
    return f'Главная страница'


@app.get("/user/admin")
async def admin_page():
    """
    Страница администратора
    """
    return f'Вы вошли как администратор'


@app.get("/user/{user_id}")
async def user_page(
        user_id: Annotated[int, Path(ge=1,
                                     le=100,
                                     description="Enter User ID",
                                     example="24"
                                     )]):
    """
    :param user_id: Целое число, >=1 и <=100
    :return:
    """
    return f'Вы вошли как пользователь № {user_id}'


@app.get("/user/{username}/{age}")
async def set_user_page(username: Annotated[str, Path(min_length=5,
                                                      max_length=20,
                                                      description="Enter username",
                                                      example="DenisStudent")],
                        age: Annotated[int, Path(ge=18,
                                                 le=120,
                                                 description="Enter age",
                                                 example="25")]):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
