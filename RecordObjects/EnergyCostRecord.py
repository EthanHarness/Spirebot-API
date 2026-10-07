from pydantic import BaseModel

class EnergyCostRecord(BaseModel):
    costsX: bool
    cost: int

    
