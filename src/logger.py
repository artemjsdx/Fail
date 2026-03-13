import logging
from datetime import datetime

# Configure the logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Create a logger object
logger = logging.getLogger(__name__)

# Example usage
if __name__ == '__main__':
    logger.info('Logger is set up and ready to use.')
    logger.debug('This is a debug message. Current datetime: %s', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    logger.critical('This is a critical message.')