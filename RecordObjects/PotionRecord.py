from pydantic import BaseModel
from typing import Dict

from .DynamicVarRecord import DynamicVarRecord


class PotionRecord(BaseModel):
    id: str
    potionUsage: str
    potionRarity: str
    targetType: str
    hasBeenRemovedFromState: bool
    dynamicVars: Dict[str, DynamicVarRecord]