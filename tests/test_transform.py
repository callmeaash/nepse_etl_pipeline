import pandas as pd
import pytest
from pipeline_utils import transform


@pytest.fixture
def sample_raw_data():
    data = {
        "symbol": ["AAPL", "AAPL", "GOOG", "GOOG"],
        "date": ["2025-01-01", "2025-01-02", "2025-01-01", "2025-01-02"],
        "open": [100, 102, 200, 202],
        "close": [101, None, 201, 203],
        "volume": [1000, None, 1500, 1600],
    }
    return pd.DataFrame(data)


def test_transform_returns_tuple(sample_raw_data):
    clean_df, technical_df = transform.transform_data(sample_raw_data)
    assert isinstance(clean_df, pd.DataFrame)
    assert isinstance(technical_df, pd.DataFrame)


def test_check_nan(sample_raw_data):
    _, technical_df = transform.transform_data(sample_raw_data)
    assert not technical_df.isnull().any().any()


def test_check_datetime(sample_raw_data):
    clean_df, _ = transform.transform_data(sample_raw_data)
    assert pd.api.types.is_datetime64_any_dtype(clean_df["date"])


def test_check_clean_data(sample_raw_data):
    clean_df, _ = transform.transform_data(sample_raw_data)
    assert len(clean_df) == sample_raw_data['symbol'].nunique()
