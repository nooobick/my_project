import customtkinter as ctk


class OperationDialog(ctk.CTkToplevel):
    def __init__(self, parent, on_submit):
        super().__init__(parent)
        self.title("Добавить операцию")
        self.geometry("420x420")
        self.resizable(False, False)
        self.on_submit = on_submit

        self.grid_columnconfigure(1, weight=1)

        fields = [
            ("Дата (YYYY-MM-DD)", "date", "2026-01-31"),
            ("Тип", "type", "expense"),
            ("Сумма", "amount", "0.00"),
            ("Описание", "description", ""),
            ("ID категории", "category", ""),
            ("ID счета", "account", "1"),
            ("ID счета назначения", "destination", ""),
        ]

        self.inputs = {}

        for row, (label, key, default) in enumerate(fields):
            ctk.CTkLabel(self, text=label).grid(row=row, column=0, padx=16, pady=8, sticky="w")
            if key == "type":
                widget = ctk.CTkOptionMenu(self, values=["expense", "income", "transfer"])
                widget.set(default)
            else:
                widget = ctk.CTkEntry(self)
                widget.insert(0, default)
            widget.grid(row=row, column=1, padx=16, pady=8, sticky="ew")
            self.inputs[key] = widget

        ctk.CTkButton(self, text="Сохранить", command=self._submit).grid(
            row=len(fields), column=0, columnspan=2, padx=16, pady=16, sticky="ew"
        )

        self.grab_set()

    def _submit(self):
        data = {
            "operation_date": self.inputs["date"].get().strip(),
            "operation_type": self.inputs["type"].get().strip(),
            "amount": self.inputs["amount"].get().strip(),
            "description": self.inputs["description"].get().strip(),
            "category_id": self.inputs["category"].get().strip(),
            "account_id": self.inputs["account"].get().strip(),
            "destination_account_id": self.inputs["destination"].get().strip(),
        }
        self.on_submit(data)
