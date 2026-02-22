import logging
from tkinter import messagebox, ttk

import customtkinter as ctk

from db.connection import DatabaseError
from services.operation_service import OperationService
from ui.dialogs.operation_dialog import OperationDialog

logger = logging.getLogger(__name__)


class OperationsView(ctk.CTkFrame):
    def __init__(self, master, operation_service: OperationService):
        super().__init__(master)
        self.operation_service = operation_service

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(20, 10))

        ctk.CTkLabel(header, text="Операции", font=ctk.CTkFont(size=22, weight="bold")).pack(side="left")
        ctk.CTkButton(header, text="Добавить", command=self.open_add_dialog).pack(side="right")

        table_wrapper = ctk.CTkFrame(self)
        table_wrapper.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        columns = ("date", "type", "amount", "category", "account", "description")
        self.tree = ttk.Treeview(table_wrapper, columns=columns, show="headings", height=16)
        headings = {
            "date": "Дата",
            "type": "Тип",
            "amount": "Сумма",
            "category": "Категория",
            "account": "Счет",
            "description": "Описание",
        }
        for col in columns:
            self.tree.heading(col, text=headings[col])
            self.tree.column(col, anchor="center")

        scrollbar = ttk.Scrollbar(table_wrapper, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.refresh_data()

    def open_add_dialog(self):
        OperationDialog(self, self._save_operation)

    def _save_operation(self, data: dict):
        try:
            self.operation_service.create_operation(**data)
            self.refresh_data()
            messagebox.showinfo("Успех", "Операция сохранена")
        except (ValueError, DatabaseError) as exc:
            logger.exception("Не удалось сохранить операцию")
            messagebox.showerror("Ошибка", str(exc))

    def refresh_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            rows = self.operation_service.list_operations()
        except DatabaseError as exc:
            logger.exception("Ошибка загрузки операций")
            messagebox.showerror("Ошибка", str(exc))
            return

        for row in rows:
            self.tree.insert(
                "",
                "end",
                values=(
                    row["operation_date"],
                    row["operation_type"],
                    row["amount"],
                    row.get("category_name") or "—",
                    row.get("account_name") or "—",
                    row.get("description") or "",
                ),
            )
