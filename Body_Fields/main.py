from fastapi import FastAPI, Body
from pydantic import Field, BaseModel
from typing import Annotated

app = FastAPI()

@app.get("/", tags=["Health"])
async def root():
    return {"message": "Hello World"}


class User(BaseModel):
    name: str | None
    username: str | None 
    bio: str | None = Field(
        title= "User bio description",
        max_length = 4000
    )
    salary: int | None = Field(
        ge=1000
    )
    age: int | None = 20

@app.put("/users/{user_id}", tags=["Users"])
async def update_user(user_id: int, user: Annotated[User, Body(embed=True)]):
    result = {
        "user_id": user_id,
        "user": user
    }
    print(result)
    return result