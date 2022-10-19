from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class PaymentValidator(BaseModel):
    payment_plan_id: int
    amount: float
    date: str
