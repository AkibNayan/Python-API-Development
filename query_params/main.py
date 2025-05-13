from fastapi import FastAPI 

app = FastAPI()

"""@app.get("/")
async def index(q:str="empty"):
    print(q)
    return {
        "message": "Hello"
    }"""

fake_item_db:list[dict[str, int]] = [{"item_name": 1}, {"item_name": 2}, {"item_name": 3}]

@app.get("/")
async def index(start:int=0, limit:int=10):
    item = fake_item_db[start:start+limit]
    return item