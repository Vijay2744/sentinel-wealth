from pydantic import BaseModel
from typing import List


class AuditRecord(BaseModel):
    decision_id: str

    customer_id: str

    timestamp: str

    policies_triggered: List[str]

    final_decision: str

    engine_version: str
