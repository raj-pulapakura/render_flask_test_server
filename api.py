from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ScoringItem(BaseModel):
    base: float
    exponent: int

@app.post("/")
async def scoring_endpoint(item: ScoringItem):
    return {
        "result": item.base**item.exponent
    }