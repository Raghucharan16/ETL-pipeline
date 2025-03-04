import sqlite3
import logging

class Loader:
    def __init__(self, config):
        self.db_path = config['paths']['output_db']
        self.table_name = config['database']['table_name']
        self.logger = logging.getLogger(__name__)

    def load_data(self, df):
        try:
            self.logger.info(f"Loading data into {self.db_path}")
            
            # Connect to database
            conn = sqlite3.connect(self.db_path)
            
            # Load data to SQLite
            df.to_sql(self.table_name, conn, if_exists='replace', index=False)
            
            # Verify load
            cursor = conn.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
            count = cursor.fetchone()[0]
            
            self.logger.info(f"Successfully loaded {count} records")
            
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Error during loading: {str(e)}")
            raise