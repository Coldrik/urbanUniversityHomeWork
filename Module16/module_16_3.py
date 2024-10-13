from fastapi import FastAPI, Path

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_user(
        username: str = Path(min_length=5, max_length=20, description='Enter username', examples='UrbanUser'),
        age: int = Path(ge=18, le=120, description='Enter age', examples='24')) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f"User {current_index} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def put_user(user_id: int = Path(ge=1, le=20, description='Enter user_id', examples='1'),
                   username: str = Path(min_length=5, max_length=20, description='Enter username', examples='UrbanUser'),
                   age: int = Path(ge=18, le=120, description='Enter age', examples='24')) -> str:
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is registered"


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=20, description='Enter user_id', examples='1')) -> str:
    del users[str(user_id)]
    return f"The user {user_id} has been deleted"
