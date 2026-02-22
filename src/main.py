import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from core.logger import setup_logging
from ui.app import FinanceApp


if __name__ == "__main__":
    setup_logging()
    app = FinanceApp()
    app.mainloop()