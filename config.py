import os
import pathlib
import logging
from dotenv import load_dotenv


# load the dotenv which reads that file and makes those values available
load_dotenv()

#Industry settings
INDUSTRY       = os.getenv("INDUSTRY","healthcare")
LEARNER_SCHEMA = os.getenv("LEARNER_SCHEMA", "leaner_47")



# File paths

# pathlib.Path(__file__) gives the path to this config.py file
# .resolve() converts it to an absolute path (no relative ".." parts)
# .parent gives the folder that config.py lives in.
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent

# The data/ folder is next to config.py in the project root.
DATA_DIR = PROJECT_ROOT / "data"             # /path/to/project/data
RAW_DATA_DIR = DATA_DIR / "raw"              # /path/to/project/data/raw
PROC_DATA_DIR = DATA_DIR / "processed"       # /path/to/project/data/processed
LOG_DIR = DATA_DIR / "logs"                  # /path/to/project/data/logs

# The  actual file paths we will read from and write to
RAW_DATA_PATH = RAW_DATA_DIR / "raw-data.csv"
PROC_DATA_PATH = PROC_DATA_DIR / "processed-data.csv"
LOG_PATH = LOG_DIR / "log.txt"

# create directories
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROC_DATA_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Database connection
DB_URL = os.getenv(
    "DB_URL",
    ""
)

try:
    from sqlalchemy import create_engine
    engine = create_engine(DB_URL, pool_pre_ping=True)
    # pool_pre_ping=True: test each connection before using it
    # If the connection dropped, SQLAlchemy gets a fresh one automatically
except Exception as _e:
    engine = None   # No database — CSV-based pipeline will still work

# Logging setup
def _setup_logger(name: str = "samuel") -> logging.Logger:
    """
    Create and configure the project logger.

    This function creates one logger that is reused everywhere.
    ALL modules import 'logger' from config.py:
        from config import logger
        logger.info("Something happened")
    """

    # create or get a logger with the given name
    lgr = logging.getLogger(name)

    # set the minimum level - messagess below INFO ae ignored
    lgr.setLevel(logging.INFO)

    # Only add handlers if none exist yet (prevent duplicate log lines)
    if not lgr.handlers:
        # Formatter defines what each log line looks like
        # %(asctime)s   → timestamp: 2026-01-15 10:23:01
        # %(levelname)s → severity:  INFO / WARNING / ERROR
        # %(message)s   → your message
        fmt = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Handler 1 — prints to terminal (existing behaviour)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(fmt)
        lgr.addHandler(console_handler)

        # Handler 2 — saves to data/logs/log.txt
        # mode="a" means append — each run adds to the file, not overwrites
        file_handler = logging.FileHandler(LOG_PATH, mode="a")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(fmt)
        lgr.addHandler(file_handler)

    return lgr

# Create the shared logger -  all modules import this
logger = _setup_logger("samuel")

# Validation thresholds
# These numbers define what counts as "acceptable" data quality.
# They are constants — all caps by Python convention — and live here
# so they can be changed in one place.
MAX_NULL_PERCENT      = 50.0   # columns with >50% nulls are flagged CRITICAL
MAX_DUPLICATE_PERCENT = 5.0    # more than 5% duplicate rows is CRITICAL