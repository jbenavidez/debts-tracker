from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class PaymentPlanValidator(BaseModel):
    id: int
    debt_id: int
    amount_to_pay: float
    installment_frequency: str
    installment_amount: float
    start_date: str
