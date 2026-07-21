from pydantic import BaseModel
from typing import Optional


class Customer(BaseModel):
    customer_id: str
    full_name: str
    age: int

    annual_income: float
    monthly_expenses: float

    total_assets: float
    total_liabilities: float

    investment_experience: str
    risk_appetite: str

    investment_horizon_years: int

    occupation: Optional[str] = None
