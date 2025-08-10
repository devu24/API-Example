from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CalcRequest(BaseModel):
    a: int
    b: int
    op: str  # "add", "subtract", "multiply", "divide"

@app.post("/calculator")
def calculate(req: CalcRequest):
    if req.op == "add":
        result = req.a + req.b
    elif req.op == "subtract":
        result = req.a - req.b
    elif req.op == "multiply":
        result = req.a * req.b
    elif req.op == "divide":
        if req.b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        result = req.a / req.b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation.")
    return {"result":result}