from pydantic import BaseModel


class Investment(BaseModel):
    investment_name: str

    investment_type: str

    amount: float

    risk_level: str

    expected_holding_years: int
