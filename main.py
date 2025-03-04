import yaml
import logging
from src.extract import Extractor
from src.transform import Transformer
from src.load import Loader

def setup_logging(config):
    logging.basicConfig(
        filename=config['paths']['log_file'],
        level=getattr(logging, config['logging']['level']),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    # Load configuration
    with open('config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    # Setup logging
    setup_logging(config)
    logger = logging.getLogger(__name__)
    
    try:
        # Initialize ETL components
        extractor = Extractor(config)
        transformer = Transformer()
        loader = Loader(config)
        
        # Execute ETL pipeline
        logger.info("Starting ETL pipeline")
        
        # Extract
        raw_data = extractor.extract_data()
        
        # Transform
        transformed_data = transformer.transform_data(raw_data)
        
        # Load
        loader.load_data(transformed_data)
        
        logger.info("ETL pipeline completed successfully")
        
    except Exception as e:
        logger.error(f"ETL pipeline failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()