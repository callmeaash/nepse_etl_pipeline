import logging
from dotenv import load_dotenv
import os
from pipeline_utils import extract

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('etl_pipeling.log'),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    extract.extract_data(os.getenv('API_KEY'))