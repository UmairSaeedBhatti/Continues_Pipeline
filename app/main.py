from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Item ID must be positive")
    if item_id > 100:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": f"Item {item_id}"}

@app.post("/items/")
async def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price must be positive")
    return item

@app.get("/users/{user_id}/items")
async def get_user_items(user_id: int, limit: int = 10):
    if user_id < 0:
        raise HTTPException(status_code=400, detail="User ID must be positive")
    return [{"item_id": i, "owner": user_id} for i in range(limit)]
