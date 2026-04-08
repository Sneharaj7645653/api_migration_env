from pydantic import BaseModel
from typing import Dict, Any, Optional

class MigrationAction(BaseModel):
    transformed_data: Dict[str, Any]

class MigrationObservation(BaseModel):
    source_data: Dict[str, Any]
    target_schema: Dict[str, Any]
    # 🔥 Add these here so they are part of the serialized object
    reward: float = 0.0
    done: bool = False