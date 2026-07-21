from pydantic import BaseModel


class Decision(BaseModel):
    decision: str

    risk_score: int

    confidence: float
