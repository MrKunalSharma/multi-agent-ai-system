import logging
import sys
from pathlib import Path
from datetime import datetime

# Create logs directory if it doesn't exist
Path("logs").mkdir(exist_ok=True)

def setup_logger(name: str) -> logging.Logger:
    """Create a logger with both file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler
    file_handler = logging.FileHandler(
        f'logs/{datetime.now().strftime("%Y%m%d")}_multiagent.log'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

# Create main logger
logger = setup_logger("MultiAgentSystem")
