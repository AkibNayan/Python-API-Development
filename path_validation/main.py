from fastapi import FastAPI, Path, status, Query
from typing import Annotated
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/", tags=["Hello"])
async def get():
    return {"Hello": "World"}

@app.get("/product/{product_id}", tags=["Get Single Product"])
async def getProduct(product_id: int):
    print(product_id)
    return {"product_id": product_id}

# Path params validation
@app.get("/user/{id}", tags=["Get Single User"])
async def getUser(id: Annotated[int, Path(title="User ID")]):
    result = {
        "user id": 1
    }
    if id:
        result.update({"path": id})
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)

# Path params and Query params validation
@app.get("/post/{id}", tags=["Get Single Post"])
async def get_post(id: Annotated[int, Path(title="Get Single Post", ge=1, le=20)], query: Annotated[str | None, Query(alias="Your Name")] = None):
    result = {
        "post id": 5
    }
    if id:
        result.update({"get a id": id})
    if query:
        result.update({"post query": query})
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)