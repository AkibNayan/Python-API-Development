from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.userSchema import userSchema

app = FastAPI()

@app.post("/", tags=["Create User"])
async def store(user:userSchema) -> userSchema:
    encoded = jsonable_encoder(user)
    return JSONResponse(status_code=status.HTTP_200_OK, content=encoded)


@app.get("/")
async def index():
    return {
        "message": "Hello World"
    }