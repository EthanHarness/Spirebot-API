from typing import List
from pydantic import BaseModel
from .CardRecord import CardRecord

class GameStateRecord(BaseModel):
    currentHp: int
    maxHp: int
    maxEnergy: int
    gold: int
    potionsSlotCount: int
    orbSlotCount: int

    drawPile: List[CardRecord]
    discardPile: List[CardRecord]
    exhaustPile: List[CardRecord]
    handPile: List[CardRecord]
    

    
