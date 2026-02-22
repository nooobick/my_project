# Рекомендуемая структура `src/`

```text
src/
  main.py                    # Точка входа
  core/
    logger.py                # Инициализация логирования
    exceptions.py            # Кастомные исключения (добавить на следующем шаге)
  db/
    connection.py            # Подключение/транзакции/контекстный менеджер
    migrations.py            # (опционально) запуск SQL миграций
  models/
    operation.py             # dataclass/DTO для операций
    ...
  repositories/
    operation_repository.py  # SQL CRUD-операции
    category_repository.py
    account_repository.py
  services/
    operation_service.py     # Бизнес-логика и валидация
    report_service.py
    forecast_service.py
  ui/
    app.py                   # Главное окно + роутинг экранов
    dialogs/
      operation_dialog.py
    views/
      operations_view.py
      statistics_view.py
      income_view.py
      categories_view.py
      accounts_view.py
      budgets_view.py
      forecast_view.py
      settings_view.py
  utils/
    export.py                # CSV/Excel экспорт
    date_tools.py
```