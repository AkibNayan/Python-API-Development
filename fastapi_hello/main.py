from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user")
async def user():
    return {
        "id": 1,
        "name": "Akib",
        "email": "akibnayan182@gmail.com",
        "password": "1234567890"
    }