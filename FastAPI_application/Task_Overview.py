import json
from functools import wraps

import aiofiles
import uvicorn
from fastapi import HTTPException, FastAPI
from pydantic import ValidationError

from errors import ValidationError, FileNotFoundError, TaskNotFoundError, UserNotFoundError


async def user_read(file_user):
    try:
        async with aiofiles.open(file_user, "r") as file:
            text = await file.read()
            return json.loads(text)
    except FileNotFoundError:
        raise "File not found"
    except json.JSONDecodeError:
        raise ValidationError("In file is JSON's error")


async def user_write(file_user, info):
    try:
        async with aiofiles.open(file_user, "w") as file:
            await file.write(json.dumps(info, indent=2))
    except FileNotFoundError:
        raise {"Error": "File not found"}
    except json.JSONDecodeError:
        raise {"Error": "In file is JSON's file"}


async def task_read(file_task):
    try:
        async with aiofiles.open(file_task, "r") as file:
            text = await file.read()
            return json.loads(text)
    except FileNotFoundError:
        raise {"Error": "File not found"}
    except json.JSONDecodeError:
        raise {"Error": "In file is JSON's error"}


async def task_write(file_task, info):
    try:
        async with aiofiles.open(file_task, "w") as file:
            await file.write(json.dumps(info, indent=2))
    except FileNotFoundError:
        raise {"Error": "File not found"}
    except json.JSONDecodeError:
        raise {"Error": "In file is JSON's file"}


app = FastAPI()

USERS_FILE = "users.json"
TASKS_FILE = "tasks.json"


def valid(func):
    @wraps(func)
    def wrapper(user):
        name = user.get("name")
        email = user.get("email")
        password = user.get("password")

        if not isinstance(name, str):
            raise HTTPException(status_code=400, detail="Name must be  string")
        if name == "":
            raise HTTPException(status_code=400, detail="Name can't be empty")
        if len(name) < 2:
            raise HTTPException(status_code=400, detail="Name can't be less then 2 characters")

        if not isinstance(email, str):
            raise HTTPException(status_code=400, detail="Email must be string")
        if email == "":
            raise HTTPException(status_code=400, detail="Email can't be empty")
        if len(email) < 8:
            raise HTTPException(status_code=400, detail="Email can't be less then 8 characters")
        if not "@" in email:
            raise HTTPException(status_code=400, detail="Not valid email must be " @ " symbol")

        if not isinstance(password, str):
            raise HTTPException(status_code=400, detail="Password must be string")
        if password == "":
            raise HTTPException(status_code=400, detail="Password can't be empty")
        if 0 < len(password) < 6:
            raise HTTPException(status_code=400, detail="Password can't be less then 8 characters")
        return wrapper

    return func


def valid_tasks(func):
    @wraps(func)
    def wrapper(task: dict):
        title = task.get("title")
        description = task.get("description")

        if not isinstance(title, str):
            raise HTTPException(status_code=400, detail="Title must be string")
        if title == "":
            raise HTTPException(status_code=400, detail="Title can't be empty")
        if len(title) < 1:
            raise HTTPException(status_code=400, detail="Title can't be less then 1 characters")

        if not isinstance(description, str):
            raise HTTPException(status_code=400, detail="Description must be string")
        if description == "":
            raise HTTPException(status_code=400, detail="Description can't be empty")
        return wrapper

    return func


@app.post("/users/register")
@valid
async def add_user(user: dict):
    try:
        new_users = await user_read(USERS_FILE)
    except FileNotFoundError as e:
        print(e)
        return {"Error": "File is not found"}
    except json.JSONDecodeError:
        new_users = []

    try:
        for u in new_users:
            if u["email"] == user["email"]:
                raise HTTPException(status_code=400, detail="Email already used")
    except ValidationError:
        return user

    new_user = max([us["id"] for us in new_users]) + 1 if new_users else 1
    user["id"] = new_user
    new_users.append(user)

    await user_write(USERS_FILE, new_users)
    return {"Register success"}


@app.post("/users/login")
@valid
async def user_login(user: dict):
    new_users = await user_read(USERS_FILE)
    try:
        for u in new_users:
            if u["email"] == user["email"] and u["password"] == user["password"]:
                return {"Login success"}
    except UserNotFoundError:
        return {"Error": "User not found"}


@app.get("/users")
async def get_users():
    new_users = await user_read(USERS_FILE)
    return new_users


@app.put("/users/{id}")
@valid
async def update_user(id: int, user: dict):
    try:
        new_users = await user_read(USERS_FILE)

        for index, new_user in enumerate(new_users):
            if new_user["id"] == id:
                new_users[index].update(user)
                await user_write(USERS_FILE, new_users)
                return new_users[index]
    except UserNotFoundError as e:
        return e
    return {"Error": "User not found"}


@app.delete("/users/{id}")
async def delete_user(id: int):
    new_users = await user_read(USERS_FILE)

    for index, new_user in enumerate(new_users):
        if new_user["id"] == id:
            deleted_user = new_users.pop(index)
            try:
                await user_write(USERS_FILE, new_users)
                return {"Deleted user": f"{deleted_user}"}
            except UserNotFoundError as e:
                return e
    return {"Error": " User not found"}

@app.get("/tasks")
async def get_tasks():
    new_tasks = await task_read(TASKS_FILE)
    return new_tasks

@app.post("/tasks")
@valid_tasks
async def add_tasks(task: dict):
    try:
        new_users = await user_read(USERS_FILE)
        new_tasks = await task_read(TASKS_FILE)

    except FileNotFoundError as e:
        print(e)
        return {"Error": "File is not found"}
    except json.JSONDecodeError:
        new_tasks = []

    try:
        for old_task in new_tasks:
            if new_tasks == old_task:
                return new_tasks.append(old_task)
            else:
                for us in new_users:
                    old_task['user_id'] == us.get('id')
                    task.update({"id": f"{old_task['user_id']}"})

    except ValidationError:
        pass

    new_tasks.append(task)
    await task_write(TASKS_FILE, new_tasks)
    return {"Register success"}


@app.put("/tasks/{id}")
@valid
async def update_task(id: int, task: dict):
    try:
        new_tasks = await task_read(TASKS_FILE)

        for index, new_task in enumerate(new_tasks):
            if new_task["id"] == id:
                new_tasks[index].update(task)
                await user_write(USERS_FILE, new_tasks)
                return new_tasks[index]
    except TaskNotFoundError as e:
        return e
    return {"Error": "Task not found"}


@app.delete("/tasks/{id}")
async def delete_task(id: int):
    new_tasks = await task_read(TASKS_FILE)

    for index, new_task in enumerate(new_tasks):
        if new_task["id"] == id:
            deleted_task = new_tasks.pop(index)
            try:
                await task_write(TASKS_FILE, new_tasks)
                return {"Deleted user": f"{deleted_task}"}
            except TaskNotFoundError as e:
                return e
    return {"Error": " Task not found"}


if __name__ == "__main__":
    uvicorn.run("Task_Overview:app", port=8090, reload=True)
