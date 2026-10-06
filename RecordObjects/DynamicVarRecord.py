from pydantic import BaseModel

class DynamicVarRecord(BaseModel):
    name: str
    baseValue: float

    
