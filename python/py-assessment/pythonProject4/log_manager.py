import logging

LOG_FILE = 'transaction.log'

def initialize_logger():
    """Set up logging to log all actions."""
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                        format='%(asctime)s - %(message)s')

def log_transaction(action):
    """Log each action performed by the user."""
    logging.info(action)
