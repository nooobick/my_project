from datetime import datetime
from decimal import Decimal, InvalidOperation

from models.operation import OperationCreate
from repositories.operation_repository import OperationRepository


class OperationService:
    ALLOWED_TYPES = {"expense", "income", "transfer"}

    def __init__(self, repository: OperationRepository) -> None:
        self.repository = repository

    def list_operations(self) -> list[dict]:
        return self.repository.list_operations()

    def create_operation(
        self,
        operation_date: str,
        operation_type: str,
        amount: str,
        description: str,
        category_id: str,
        account_id: str,
        destination_account_id: str,
    ) -> int:
        if operation_type not in self.ALLOWED_TYPES:
            raise ValueError("Недопустимый тип операции")

        try:
            parsed_date = datetime.strptime(operation_date, "%Y-%m-%d").date()
        except ValueError as exc:
            raise ValueError("Дата должна быть в формате YYYY-MM-DD") from exc

        try:
            parsed_amount = Decimal(amount)
        except (InvalidOperation, ValueError) as exc:
            raise ValueError("Сумма должна быть числом") from exc

        if parsed_amount <= 0:
            raise ValueError("Сумма должна быть больше 0")

        try:
            parsed_account_id = int(account_id)
        except ValueError as exc:
            raise ValueError("ID счета должен быть числом") from exc

        parsed_category_id = int(category_id) if category_id else None
        parsed_destination_id = int(destination_account_id) if destination_account_id else None

        payload = OperationCreate(
            operation_date=parsed_date,
            operation_type=operation_type,
            amount=parsed_amount,
            description=description.strip(),
            category_id=parsed_category_id,
            account_id=parsed_account_id,
            destination_account_id=parsed_destination_id,
        )
        return self.repository.create_operation(payload)
