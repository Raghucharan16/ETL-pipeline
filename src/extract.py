import pandas as pd
import logging

class Extractor:
    def __init__(self, config):
        self.input_file = config['paths']['input_file']
        self.logger = logging.getLogger(__name__)

    def extract_data(self):
        try:
            self.logger.info(f"Extracting data from {self.input_file}")
            df = pd.read_csv(self.input_file)
            self.logger.info(f"Successfully extracted {len(df)} records")
            return df
        except Exception as e:
            self.logger.error(f"Error during extraction: {str(e)}")
            raise