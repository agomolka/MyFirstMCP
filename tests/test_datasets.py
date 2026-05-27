from first_mcp_insights.datasets import (
    ensure_sample_dataset,
    list_csv_datasets,
    load_dataset,
)

def test_sample_dataset_is_created() -> None:
    path = ensure_sample_dataset()

    assert path.exists()
    assert path.name == "iris.csv"

def test_list_csv_datasets_contains_iris() -> None:
    dataset = list_csv_datasets()
    assert "iris.csv" in dataset

def test_load_dataset_returns_dataframe() -> None:
    df = load_dataset("iris.csv")

    assert not df.empty
    assert "target_name" in df.columns