from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Annotated


app = FastAPI()

@app.get("/")
async def root_route():
    return {"message": "Hello World"}


#Update a User
"""@app.put("/{id}", tags=["update user"])
async def update_user(id: int, query: str):
    print(id)
    print(query)
    return {"update": "user"}"""


class User(BaseModel):
    name: str | None = None
    username: str
    email: str
    password: str
    age: int | None = 20


@app.put("/{id}", tags=["update user"])
async def update_user(id: Annotated[int, Path(title="User ID", ge=0, le=100)], query: Annotated[str, Query(title="Search Query",  pattern="^akib$")], user: User | None = None):
    print(id)
    print(query)
    print(user)
    return {"update": "user"}