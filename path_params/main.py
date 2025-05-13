from fastapi import FastAPI, status
from fastapi.responses import JSONResponse 
from enum import Enum 

app = FastAPI()

@app.get("/")

async def health():
    return {
        "message": "Hello"
    }
    
class Role(str, Enum):
    ADMIN="ADMIN"
    USER="USER"
@app.get("/user/{Role}")
async def user(role:Role):
    if role is role.ADMIN:
        return JSONResponse(status_code=status.HTTP_200_OK, content={
        "message": "Welcome Admin"
    })
    else:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
            "message": "Sorry! you are not admin"
        })
    

