import logging

from src.core.config import settings
from src.server import create_server

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(settings.NAME)

mcp = create_server()

if __name__ == "__main__":
    logger.info(f"starting {mcp.settings.host}:{mcp.settings.port}")
    mcp.run(transport="stdio")
