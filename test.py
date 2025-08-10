from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/devendra/yadav")
def add(a:int,b:int):
    return a + b
# print(add(5, 22))

class Item(BaseModel):
    a: int
    b: int

def subtract(a: int, b: int):
    return a - b


@app.post("/subtract")
def subtract_endpoint(Model: Item):
    return subtract(Model.a, Model.b)

@app.post("/multiply")
def multiply_endpoint(Model: Item):
    return Model.a * Model.b