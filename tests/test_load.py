import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from pipeline_utils import load


@pytest.fixture
def sample_clean_data():
    return pd.DataFrame({
        "symbol": ["HDBL", "HPC"],
        "date": pd.to_datetime(["2024-01-01", "2024-01-02"]),
        "open": [100, 110],
        "high": [105, 115],
        "low": [95, 105],
        "close": [102, 112],
        "volume": [1000, 2000]
    })


@pytest.fixture
def sample_technical_data():
    return pd.DataFrame({
        "indicator": ["RSI", "MACD"],
        "value": [45.5, 0.12]
    })


@patch("pipeline_utils.load.os.makedirs")
@patch("pipeline_utils.load.create_engine")
@patch("pipeline_utils.load.pd.read_sql")
@patch("pipeline_utils.load.pd.DataFrame.to_csv")
@patch("pipeline_utils.load.pd.DataFrame.to_sql")
def test_load_data_success(
    mock_to_sql, mock_to_csv, mock_read_sql, mock_create_engine, mock_makedirs,
    sample_clean_data, sample_technical_data
):
    fake_engine = MagicMock()
    mock_create_engine.return_value = fake_engine

    mock_read_sql.return_value = pd.DataFrame({"id": [1, 2], "symbol": ["HDBL", "HPC"]})

    load.load_data(sample_clean_data, sample_technical_data)

    mock_makedirs.assert_called_once()

    mock_to_csv.assert_called_once()

    assert mock_to_sql.call_count == 1

    mock_read_sql.assert_called_once()

    mock_create_engine.assert_called_once()
