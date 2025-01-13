from fastapi import FastAPI

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
async def user_page(user_id):
    """
    Страница пользователя по **id**
    """
    return f'Вы вошли как пользователь № {user_id}'


@app.get("/user")
async def set_user_page(username: str, age: int):
    """
    Страница якобы авторизованного пользователя
    - **username**: Имя
    - **age**: Возраст
    """
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'