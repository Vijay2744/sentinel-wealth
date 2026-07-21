from pydantic import BaseModel
from typing import List


class Recommendation(BaseModel):
    summary: str

    reasons: List[str]

    suggested_actions: List[str]
