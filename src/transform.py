import pandas as pd
import logging

class Transformer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def transform_data(self, df):
        try:
            self.logger.info("Starting data transformation")
            
            # Clean and transform data
            df_transformed = df.copy()
            
            # Convert date to datetime
            df_transformed['date'] = pd.to_datetime(df_transformed['date'])
            
            # Handle missing values
            df_transformed['quantity'] = df_transformed['quantity'].fillna(0)
            df_transformed['price'] = df_transformed['price'].fillna(df_transformed['price'].mean())
            
            # Calculate total amount
            df_transformed['total_amount'] = df_transformed['quantity'] * df_transformed['price']
            
            # Standardize product names
            df_transformed['product'] = df_transformed['product'].str.lower().str.strip()
            
            self.logger.info("Data transformation completed")
            return df_transformed
            
        except Exception as e:
            self.logger.error(f"Error during transformation: {str(e)}")
            raise