from models.operation import OperationCreate
from db.connection import db_cursor


class OperationRepository:
    def list_operations(self) -> list[dict]:
        query = """
        SELECT
            o.id,
            o.operation_date,
            o.operation_type,
            o.amount,
            o.description,
            c.name AS category_name,
            a.name AS account_name,
            da.name AS destination_account_name
        FROM operations o
        LEFT JOIN categories c ON c.id = o.category_id
        INNER JOIN accounts a ON a.id = o.account_id
        LEFT JOIN accounts da ON da.id = o.destination_account_id
        ORDER BY o.operation_date DESC, o.id DESC
        """
        with db_cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def create_operation(self, payload: OperationCreate) -> int:
        query = """
        INSERT INTO operations (
            operation_date, operation_type, amount, description,
            category_id, account_id, destination_account_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        with db_cursor(commit=True) as cursor:
            cursor.execute(
                query,
                (
                    payload.operation_date,
                    payload.operation_type,
                    payload.amount,
                    payload.description,
                    payload.category_id,
                    payload.account_id,
                    payload.destination_account_id,
                ),
            )
            return cursor.lastrowid