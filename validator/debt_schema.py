from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

class DebtValidator(BaseModel):
    id: int
    amount: float
