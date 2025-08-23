from unittest.mock import patch, MagicMock
import pandas as pd
from pipeline_utils import extract


def test_extract_data_success():
    with patch("pandas.read_csv") as mock_read_csv, \
         patch("requests.get") as mock_get:
        
        mock_read_csv.return_value = pd.DataFrame({"Symbol": ["NHPC", "BPCL"]})

        response = MagicMock()
        response.json.return_value = [{"date": "2025-01-01", "price": 100}] * 200
        mock_get.return_value = response

        df = extract.extract_data("http://fakeapi.com")
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 200 * 2
