from typing import Dict, List

from pydantic import BaseModel
from .EnergyCostRecord import EnergyCostRecord
from .DynamicVarRecord import DynamicVarRecord
from .EnchantmentRecord import EnchantmentRecord

class CardRecord(BaseModel):
    id: str
    type: str
    energyCost: EnergyCostRecord
    targetType: str
    keywords: List[str]
    tags: List[str]
    dynamicVars: Dict[str, DynamicVarRecord]
    enchantment: EnchantmentRecord|None
    affliction: str|None
    isUpgraded: bool
    baseReplayCount: int
    shouldRetainThisTurn: int
    isSlyThisTurn: bool
    gainsBlock: bool
    orbEvokeType: str
    exhaustOnNextPlay: bool
    currentStarCost: int
    


