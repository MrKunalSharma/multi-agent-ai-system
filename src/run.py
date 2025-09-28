import uvicorn
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.api.main import app
from src.core.logger import logger

if __name__ == "__main__":
    logger.info("Starting Multi-Agent AI System API...")
    
    # Run with the app object directly (no reload)
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
