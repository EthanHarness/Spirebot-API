from pydantic import BaseModel

class ModelRecord(BaseModel):
    category: str
    entry: str

class EnchantmentRecord(BaseModel):
    id: ModelRecord
    amount: int

    
