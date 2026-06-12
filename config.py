from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

DEMO_USERS_FILE = DATA_DIR / "demo_users.json"
WORDLISTS_DIR = DATA_DIR / "wordlists"
COMMON_PATTERNS_FILE = DATA_DIR / "common_patterns.txt"
RESULTS_CSV = OUTPUT_DIR / "results.csv"
RESULTS_JSON = OUTPUT_DIR / "results.json"

DEFAULT_DELAY_MS = 20
DEFAULT_USERS_TO_GENERATE = 12
DEFAULT_PROGRESS_REFRESH = 10
