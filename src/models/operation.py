from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(slots=True)
class OperationCreate:
    operation_date: date
    operation_type: str
    amount: Decimal
    description: str
    category_id: int | None
    account_id: int
    destination_account_id: int | None = None