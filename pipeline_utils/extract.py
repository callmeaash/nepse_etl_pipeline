import requests
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
        raise

    # Read data from the api for each stock, convert into Dataframe and append into a list
    all_dfs = []
    logger.info("Attempting to extract data...")
    for stock in tickers['Symbol']:
        try:
            response = requests.get(api_url + stock)
            data = response.json()
            df = pd.DataFrame(data[:200])
            all_dfs.append(df)

        except requests.RequestException as e:
            logger.error(f"Failed to fetch stock data: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected error occured: {e}")

    # Concate the Dataframes from the list into one
    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
        logger.info(f"Combined Dataframe contains: {len(combined_df)} rows")
        return combined_df
    else:
        logger.error("No stock data fetched")
        raise ValueError('Not stock data fetched')
