from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()


@app.get("/", tags=["health"])
async def health():
    return {"status": "ok"}

fake_data: dict[str, list[dict[str, str]]] = {
    "items": [
        {"item1": "Apple"},
        {"item2": "Banana"}
    ]
}


"""@app.get("/items", tags=["Items"])
async def get_items(q: str | None = None):
    print(q)
    return {"hello": "world"}"""


"""@app.get("/items", tags=["Items"])
async def get_items(query: str | None = None):
    print(query)
    if query:
        fake_data.update({"query": query})
    return fake_data"""


# Annotated Validation Apply
"""@app.get("/items", tags=["Items"])
async def get_items(query: Annotated[str | None, Query(max_length=10, min_length=3, pattern="^akib$")] = None):
    print(query)
    if query:
        fake_data.update({"query": query})
    return fake_data"""


# Handle list, dict
"""@app.get("/items", tags=["Items"])
async def get_items(query: Annotated[list[str], Query()] = None):
    print(query)
    if query:
        fake_data.update({"query": query})
    return fake_data"""


# Handle Metadata
@app.get("/items", tags=["Items"])
async def get_items(query: Annotated[str, Query(title="Get All item", description="This is a description", alias="Akib-Nayan", deprecated=False)] = None):
    print(query)
    if query:
        fake_data.update({"query": query})
    return fake_data
