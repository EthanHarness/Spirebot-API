from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# # 1. Define data model schema
# class Item(BaseModel):
#     id: int
#     name: str
#     price: float
#     description: Optional[str] = None

# # In-memory database simulation
# db: List[Item] = [
#     Item(id=1, name="Laptop", price=999.99, description="High-performance laptop"),
#     Item(id=2, name="Mouse", price=25.50, description="Wireless optical mouse")
# ]

# # 2. READ (GET) All Items
# @app.get("/items", response_model=List[Item])
# def get_items():
#     return db

# # 3. READ (GET) a Single Item by ID
# @app.get("/items/{item_id}", response_model=Item)
# def get_item(item_id: int):
#     for item in db:
#         if item.id == item_id:
#             return item
#     raise HTTPException(status_code=404, detail="Item not found")

# # 4. CREATE (POST) a New Item
# @app.post("/items", response_model=Item, status_code=201)
# def create_item(item: Item):
#     # Check if item ID already exists
#     if any(x.id == item.id for x in db):
#         raise HTTPException(status_code=400, detail="Item ID already exists")
#     db.append(item)
#     return item

# # 5. DELETE (DELETE) an Item
# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     for idx, item in enumerate(db):
#         if item.id == item_id:
#             del db[idx]
#             return {"message": "Item successfully deleted"}
#     raise HTTPException(status_code=404, detail="Item not found")


class ContextResponse(BaseModel):
    context: str

class CardRecord(BaseModel):
    Id: str

class GameState(BaseModel):
    CurrentHp: int
    MaxHp: int
    MaxEnergy: int
    Gold: int
    PotionsSlotCount: int
    OrbSlotCount: int

    DrawPile: List[CardRecord]
    DiscardPile: List[CardRecord]
    ExhaustPil: List[CardRecord]

#TODO: Parse input into objects
@app.post("/context", status_code=201)
async def repeat_context(game_state: Request):
    body_bytes = await game_state.body()
    game_state_str = body_bytes.decode('utf-8')

    print("HERE")
    print(game_state_str)
    
    return {"context": "Random Stuff"}