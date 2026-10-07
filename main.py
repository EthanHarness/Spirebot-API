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

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional

from RecordObjects.GameStateRecord import GameStateRecord

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print("\n❌ --- FASTAPI VALIDATION ERROR ---")
    for error in exc.errors():
        # Prints exactly which field failed and why
        print(f"Location: {error['loc']}")
        print(f"Error Message: {error['msg']}")
        print(f"Type of Error: {error['type']}\n")
    print("-----------------------------------\n")
    
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

class ContextResponse(BaseModel):
    context: str

@app.post("/context", status_code=201)
async def repeat_context(game_state: GameStateRecord):
    print(game_state)
    
    return {"context": "Random Stuff"}

#TODO: Parse input into objects
# @app.post("/context", status_code=201)
# async def repeat_context(game_state: Request):
#     body_bytes = await game_state.body()
#     game_state_str = body_bytes.decode("utf-8")
    
#     print(game_state_str)
    
#     return {"context": "Random Stuff"}