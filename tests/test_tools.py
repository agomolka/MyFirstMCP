from first_mcp_insights.tools import (
    compute_correlation_tool,
    dataset_profile_tool,
    get_columns_tool,
    preview_dataset_tool,
    value_counts_tool,
)

def test_dataset_profile_tool() -> None:
    profile = dataset_profile_tool("iris.csv")
    
    assert profile["dataset"] == "iris.csv"
    assert profile["rows"] > 0
    assert profile["columns"] > 0

def test_get_columns_tool() -> None:
    columns = get_columns_tool("iris.csv")

    assert "numeric_columns" in columns
    assert "categorical_columns" in columns

def test_preview_dataset_tool() -> None:
    rows = preview_dataset_tool("iris.csv", rows=3)

    assert len(rows) == 3
    assert isinstance(rows[0], dict)

def test_compute_correlation_tool() -> None:
    result = compute_correlation_tool(
        dataset_name="iris.csv",
        column_a="petal length (cm)",
        column_b="petal width (cm)",
    )

    assert result["dataset"] == "iris.csv"
    assert "pearson_correlation" in result

def test_value_counts_tool() -> None:
    result = value_counts_tool("iris.csv", "target_name")

    assert result["dataset"] == "iris.csv"
    assert result["column"] == "target_name"
    assert "value_counts" in result