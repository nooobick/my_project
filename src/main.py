import sys
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.logger import setup_logging
from src.ui.app import FinanceApp


if __name__ == "__main__":
    setup_logging()
    app = FinanceApp()
    app.mainloop()