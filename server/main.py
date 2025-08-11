#!/usr/bin/env python3
"""
Chess Game Server - Railway Production Entry Point
"""

import os
import sys
import logging
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Import the server
from improved_game_server import run_server
import asyncio

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def main():
    """Main entry point for Railway deployment"""
    print("🚀 Starting Chess Game Server on Railway...")
    print(f"Environment: {os.getenv('RAILWAY_ENVIRONMENT', 'local')}")
    print(f"Host: {os.getenv('HOST', '0.0.0.0')}")  
    print(f"Port: {os.getenv('PORT', '8000')}")
    print("📋 Python version:", sys.version)
    print("📂 Current directory:", os.getcwd())
    
    logger.info("🚀 Starting Chess Game Server on Railway...")
    logger.info(f"Environment: {os.getenv('RAILWAY_ENVIRONMENT', 'local')}")
    logger.info(f"Host: {os.getenv('HOST', '0.0.0.0')}")  
    logger.info(f"Port: {os.getenv('PORT', '8000')}")
    
    try:
        print("🔄 About to start asyncio.run(run_server())")
        logger.info("🔄 About to start asyncio.run(run_server())")
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("👋 Server stopped by user")
        logger.info("👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")
        logger.error(f"❌ Server error: {e}")
        import traceback
        print("Full traceback:")
        traceback.print_exc()
        logger.error("Full traceback: %s", traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
