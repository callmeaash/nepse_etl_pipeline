import logging
from dotenv import load_dotenv
import os
from pipeline_utils import extract, transform, load


def run_etl():
    load_dotenv()
    api_url = os.getenv('API_KEY')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('etl_pipeline.log')
        ]
    )

    raw_data = extract.extract_data(api_url)
    clean_data, technical_data = transform.transform_data(raw_data)
    load.load_data(clean_data, technical_data)

if __name__ == "__main__":
    run_etl()