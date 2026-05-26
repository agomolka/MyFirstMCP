from typing import Any
import pandas as pd

from first_mcp_insights.config import MAX_PREVIEW_ROWS, SAMPLE_DATASET_NAME
from first_mcp_insights.datasets import (
    categorical_columns, dataset_profile, list_csv_datasets,
    load_dataset, numeric_columns
)

def list_dataset_tool() -> list[str]:
    """List available CSV datasets."""
    return list_csv_datasets

def dataset