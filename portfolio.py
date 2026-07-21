from pydantic import BaseModel


class Portfolio(BaseModel):
    cash: float
    equity: float
    mutual_funds: float
    fixed_income: float
    gold: float
    real_estate: float
