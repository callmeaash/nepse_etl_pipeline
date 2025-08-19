
import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

def extract_data(api_url: str) -> pd.DataFrame:
    """
    Fetch data from API and Return as Dataframe
    """

    stocks_file = os.path.abspath(os.path.join('stock_names_data', 'hydropower.csv'))

    try:
        logger.info(f"Attempting to read tickers from {stocks_file}")
        tickers = pd.read_csv(stocks_file)
        logger.info(f"Successfully read the tickers from {stocks_file}")

    except FileNotFoundError:
        logger.error("Stocks file not found")
    

