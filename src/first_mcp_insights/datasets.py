from pathlib import Path
from typing import Any

import pandas as pd
from sklearn.datasets import load_iris

from first_mcp_insights.config import (DATA_DIR, SAMPLE_DATASET_PATH, SAMPLE_DATASET_NAME)

def ensure_data_dir() -> None:
    """Ensure the local data directory exists."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def create_sample_iris_dataset() -> Path:
    """Create the Iris sample dataset as a local CSV file.
    Returns:
        Path to the generated CSV file.
    """
    ensure_data_dir()

    if SAMPLE_DATASET_PATH.exists():
        return SAMPLE_DATASET_PATH
    
    iris = load_iris(as_frame=True)
    df = iris.frame.copy()

    target_mapping = dict(enumerate(iris.target_names))
    df["target_name"] = df["target"].map(target_mapping)

    df.to_csv(SAMPLE_DATASET_PATH, index=False)
    return SAMPLE_DATASET_PATH

def ensure_sample_dataset() -> Path:
    """Ensure the sample Iris dataset exists."""
    return create_sample_iris_dataset

def list_csv_datasets() -> list[str]:
    """List available CSV datasets in the data directory."""
    ensure_sample_dataset()
    return sorted(path.name for path in DATA_DIR.glob(".csv"))

def safe_dataset_path(dataset_name: str) -> Path:
    """Retur a safe local dataset path.

    This prevents path traversal by only allowing filenames inside data.
    """
    ensure_data_dir()

    safe_name = Path(dataset_name).name
    path = DATA_DIR / safe_name

    if path.suffix.lower() != ".csv":
        raise ValueError("Only CSV files are supported.")
    
    if not path.exists():
        available = ", ".join(list_csv_datasets())
        raise FileNotFoundError(f"Dataset '{safe_name}' was not found. Available datasets: {available}")
    
    return path

def load_dataset(dataset_name: str = SAMPLE_DATASET_NAME) -> pd.DataFrame:
    """Load a CSV dataset from the local data directory."""
    path = safe_dataset_path(dataset_name)
    return pd.read_csv(path)

def dataset_profile(dataset_name: str) -> dict[str, Any]:
    """Return a compact profile of a dataset."""
    df = load_dataset(dataset_name)

    missing_values = {
        column: int(count)
        for column, count in df.isna().sum().items()
    }

    return {
        "dataset": dataset_name,
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "dtype": {
            column: str(dtype)
            for column, dtype in df.dtypes.items()
        },
        "missing_values": missing_values,
    }

def numeric_columns(dataset_name: str) -> list[str]:
    """Return numeric columns for a dataset."""
    df = load_dataset(dataset_name)
    return list(df.select_dtypes(include="number").columns)

def categorical_columns(dataset_name: str) -> list[str]:
    """Return non-numeric columns for a dataset."""
    df = load_dataset(dataset_name)
    return list(df.select_dtypes(exclude="number").columns)