import customtkinter as ctk

from src.repositories.operation_repository import OperationRepository
from src.services.operation_service import OperationService
from src.ui.views.operations_view import OperationsView


class FinanceApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Учет личных финансов")
        self.geometry("1200x720")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.operation_service = OperationService(OperationRepository())

        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.sidebar.grid_propagate(False)

        ctk.CTkLabel(
            self.sidebar,
            text="Finance Control",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).pack(pady=(24, 16), padx=16)

        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=0, column=1, sticky="nsew")

        self.screens = {}
        menu_items = [
            ("Операции", self.show_operations),
            ("Статистика", self.show_placeholder),
            ("Доходы", self.show_placeholder),
            ("Категории", self.show_placeholder),
            ("Счета", self.show_placeholder),
            ("Бюджеты", self.show_placeholder),
            ("Прогноз", self.show_placeholder),
            ("Настройки", self.show_placeholder),
        ]
        for title, callback in menu_items:
            ctk.CTkButton(self.sidebar, text=title, command=lambda cb=callback, t=title: cb(t)).pack(
                fill="x", padx=12, pady=6
            )

        self.show_operations("Операции")

    def _clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_operations(self, _=None):
        self._clear_content()
        OperationsView(self.content, self.operation_service).pack(fill="both", expand=True)

    def show_placeholder(self, title: str):
        self._clear_content()
        wrapper = ctk.CTkFrame(self.content, fg_color="transparent")
        wrapper.pack(fill="both", expand=True)
        ctk.CTkLabel(
            wrapper,
            text=f"Экран «{title}» будет реализован следующим шагом",
            font=ctk.CTkFont(size=20),
        ).pack(pady=40)
