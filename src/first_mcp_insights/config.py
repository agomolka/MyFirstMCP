from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_DIR.parents[1]

DATA_DIR = PROJECT_ROOT / "data"
SAMPLE_DATASET_NAME = "iris.csv"
SAMPLE_DATASET_PATH = DATA_DIR / SAMPLE_DATASET_NAME

MAX_PREVIEW_ROWS = 10