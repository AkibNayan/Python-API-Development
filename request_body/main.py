from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.userSchema import UserSchema



app = FastAPI()
@app.post("/", tags = ["User Create"])
async def store(user: UserSchema):
    encoded = jsonable_encoder(user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=encoded)


@app.get("/")
async def index():
    return {
        "message": "Hello World"
    }
    