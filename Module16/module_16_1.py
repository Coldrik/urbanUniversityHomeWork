from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def user_id(user_id: str) -> str:
    return f"Вы вошли как {user_id}"

@app.get("/user")
async def user_id(username: str, age: int) -> str:
    return f"Информация о пользователе: {username}, Возвраст {age}"