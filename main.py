from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.calculator import calculate_npi

app = FastAPI()

# ====================
# --- API TEST ---
# ====================

class Item(BaseModel):
    text: str
    is_done : bool = False

items = []

@app.get("/")
def root(): 
    return {"message": "Hello World"}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[:limit]

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int) -> Item: 
    if item_id < len(items):
        return items[item_id]
    else: 
        raise HTTPException(status_code=404, detail="Item not found")
    

# ====================
# --- API NPI ---
# ====================

class NPIExpression(BaseModel):
    expression: str

@app.post("/calculate")
def calculate_expression(expression: NPIExpression):
    try:
        result = calculate_npi(expression.expression)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))