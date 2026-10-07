from pydantic import BaseModel
from typing import Dict

from .DynamicVarRecord import DynamicVarRecord


class RelicRecord(BaseModel):
    id: str
    status: str
    isTradeable: bool
    isUsedUp: bool
    showCounter: bool
    displayAmount: int
    isWax: bool
    isMelted: bool
    hasBeenRemovedFromState: bool
    dynamicVars: Dict[str, DynamicVarRecord]