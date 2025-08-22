import pandas as pd
from sqlalchemy import create_engine
import logging
import os

logger = logging.getLogger(__name__)


def load_data(clean_data: pd.DataFrame, technical_data: pd.DataFrame) -> None:
    """
    Load the data into the database and store in file
    """

    logger.info('Creating a folder to store clean data')
    transformed_data_dir = os.path.join('clean_data')
    try:
        os.makedirs(transformed_data_dir, exist_ok=True)
        logger.info(f'Directory created or already exists: {transformed_data_dir}')
    except Exception as e:
        logger.error(f'Failed to create directory: {e}')
        raise
    
    # Storing the technical data into a csv file
    logger.info("Attempting to store the technical_data df")
    technical_data_path = os.path.join(transformed_data_dir, 'technical_data.csv')
    try:
        technical_data.to_csv(technical_data_path, index=False)
        logger.info(f'Technical data stored at {technical_data_path}')
    except Exception as e:
        logger.error(f'Failed to save the technical data: {e}')
        raise

    # Creating a connection to the postgresql
    try:
        logger.info("Attempting to create a connection to the database")
        database_url = os.getenv('DATABASE_URL')
        engine = create_engine(database_url)
        logger.info(f'Successfully connected to {database_url}')
    except Exception as e:
        logger.error(f'Failed to create the connection: {e}')
        raise
    
    # Inserting the OHLC data into the database
    stocks_symbol = clean_data[['symbol']]
    try:
        logger.info("Appending the stocks symbol in the stocks table")
        stocks_symbol.to_sql('stocks', engine, if_exists='append', index=False)
    except Exception as e:
        logger.error(f"Error occured when appending the stocks symbol: {e}")
        raise
    
    try:
        logger.info("Inserting the ohlc data into ohlc table")
        stocks_id_from_db = pd.read_sql("SELECT id, symbol FROM stocks", engine)
        ohlc_data = clean_data.merge(stocks_id_from_db, on='symbol', how='left')
        ohlc_data.rename(columns={'id': 'stock_id'}, inplace=True)
        ohlc_data.drop(columns=['symbol'], inplace=True)
        ohlc_data.to_sql('ohlc', engine, if_exists='append', index=False)
        logger.info(f"Inserted {len(ohlc_data)} rows into the ohlc table")
    except Exception as e:
        logger.error(f"Error inserting ohlc data in ohlc table: {e}")
        raise

    logger.info("Completed Loading the data")
