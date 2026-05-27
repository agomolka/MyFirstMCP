from mcp.server.fastmcp import FastMCP

from first_mcp_insights.datasets import ensure_sample_dataset, load_dataset
from first_mcp_insights.tools import (
    compute_correlation_tool,
    dataset_profile_tool,
    describe_dataset_tool,
    filter_rows_tool,
    get_columns_tool,
    list_dataset_tool,
    preview_dataset_tool,
    value_counts_tool,
)

mcp = FastMCP(
    name = "first-mcp-insights",
    instructions = (
        "A beginner-friendly data science MCP server."
        "Use it to inspect CSV datasets, preview rows, compute statistics, "
        "filter rows, and calculate correlation."
    ),
)

@mcp.tool()
def list_datasets() -> list[str]:
    """List available CSV datasets."""
    return list_dataset_tool()

@mcp.tool()
def dataset_profile(dataset_name: str = "iris.csv") -> dict:
    """Return rows, columns, dtype, and missing-value counts for a dataset."""
    return get_columns_tool(dataset_name)

@mcp.tool()
def get_columns(dataset_name: str ="iris.csv") -> dict:
    """Return numeric and categorical columns for a dataset."""
    return get_columns_tool(dataset_name)

@mcp.tool()
def preview_dataset(dataset_name: str = "iris.csv", rows: int = 5) -> dict:
    """Preview the first rows of dataset."""
    return preview_dataset_tool(dataset_name, rows)

@mcp.tool()
def describe_dataset(dataset_name: str = "iris.csv") -> dict:
    """Return descriptive statistics for a dataset."""
    return describe_dataset_tool(dataset_name)

@mcp.tool()
def compute_correlation(
    dataset_name: str,
    column_a: str,
    column_b: str,
) -> dict:
    """Compute Pearson correlation between two numeric columns."""
    return compute_correlation_tool(dataset_name, column_a, column_b)

@mcp.tool()
def filter_rows(
    dataset_name: str,
    column: str,
    value: str,
    limit: int = 5,
) -> list[dict]:
    """Filter rows where a column equals a specific value."""
    return filter_rows_tool(dataset_name, column, value, limit)

@mcp.tool()
def value_counts(
    dataset_name: str,
    column: str,
    limit: int = 10,
) -> dict:
    """Return most common values for a column."""
    return value_counts_tool(dataset_name, column, limit)

@mcp.resource("dataset://iris")
def iris_dataset_resource() -> str:
    """Provide a simple text resource describing the Iris dataset."""
    ensure_sample_dataset()
    df = load_dataset("iris.csv")

    return (
        f"The Iris dataset has {len(df)} rows and {len(df.columns)} columns. "
        f"Columns: {', '.join(df.columns)}."
    )

@mcp.prompt()
def explore_dataset_prompt(dataset_name: str = "iris.csv") -> str:
    """Prompt template for exploring a dataset."""
    return (
        f"Explore the dataset named {dataset_name}. "
        "First list its columns, then summarize its shape, missing values, "
        "numeric columns, categorical columns, and any interesting correlations."
    )

def main() -> None:
    """Run the MCP server."""
    ensure_sample_dataset()
    mcp.run()

if __name__ == "__main__":
    main()