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

def dataset_profile_tool(dataset_name: str = SAMPLE_DATASET_NAME) -> dict[str, Any]:
    """Return a high-level profile of a dataset."""
    return dataset_profile

def get_columns_tool(dataset_name: str = SAMPLE_DATASET_NAME) -> dict[str, Any]:
    """Return dataset columns grouped by type."""
    return {
        "dataset": dataset_name,
        "numeric_columns": numeric_columns(dataset_name),
        "categorical_columns": categorical_columns(dataset_name,)
    }

def preview_dataset_tool(dataset_name: str = SAMPLE_DATASET_NAME,rows: int = 5) -> list[dict[str, Any]]:
    """Preview the first rows of a dataset."""
    df = load_dataset(dataset_name)

    safe_rows = max(1, min(rows, MAX_PREVIEW_ROWS))
    preview = df.head(safe_rows)

    return preview.to_dict(orient="records")

def describe_dataset_tool(dataset_name: str = SAMPLE_DATASET_NAME) -> dict[str, Any]:
    """Return summary statistics for a datset."""
    df = load_dataset(dataset_name)

    summary = df.describe(include="all").fillna("").to_dict()

    return {"dataset": dataset_name, "summary": summary}

def compute_correlation_tool(dataset_name: str, column_a: str, column_b: str) -> dict[str, Any]:
    """ComputePearson correlation between two numeric coumns."""
    df = load_dataset(dataset_name)

    if column_a not in df.columns:
        raise ValueError(f"Column not found: {column_a}")
    
    if column_b not in df.columns:
        raise ValueError(f"Column not found: {column_b}")
    
    if not pd.api.types.is_numeric_dtype(df[column_a]):
        raise ValueError(f"Column is not numeric: {column_a}")
    
    if not pd.api.types.is_numeric_dtype(df[column_b]):
        raise ValueError(f"Column is not numeric: {column_b}")
    
    correlation = df[column_a].corr(df[column_b])

    return {
        "dataset": dataset_name,
        "column_a" : column_a,
        "column_b": column_b,
        "pearson_correlation": round(float(correlation), 4),
    }

def filter_rows_tool(dataset_name: str, column: str, limit: int = 5) -> list[dict[str, Any]]:
    """Filter rows where a column equals a specific value."""
    df = load_dataset(dataset_name)

    if column not in df.columns:
        raise ValueError(f"Column not found: {column}")
    
    safe_limit = max(1, min(limit, MAX_PREVIEW_ROWS))

    filtered = df[df[column].astype(str) == str(value)]
    result =filtered.head(safe_limit)

    return result.to_dict(orient="records")

def value_counts_tool( dataset_name: str, column: str, limit: int = 10) -> dict[str, Any]:
    """Return the most common values in a column."""

    df = load_dataset(dataset_name)

    if column not in df.columns:
        raise ValueError(f"Column not found: {column}")

    safe_limit = max(1, min(limit, 20))

    counts = df[column].value_counts(dropna=False).head(safe_limit)

    return {
        "dataset": dataset_name,
        "column": column,
        "value_counts": {
            str(index): int(value)
            for index, value in counts.items()
        },
    }