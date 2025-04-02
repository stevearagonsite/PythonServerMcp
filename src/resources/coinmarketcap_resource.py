https://coinmarketcap.com/
"""System resources for the MCP server."""

import logging
from typing import List

from ..services import get_cryptocurrency_data

# Configure logging
logger = logging.getLogger(__name__)


def register_resources(server):
    """
    Register all system resources with the server.

    Args:
        server: MCP server instance
    """

    @server.resource("file://assets/coinmarketcap-docs.txt")
    def get_file_docs() -> list[str]:
        """
        Get cryptocurrency data.

        Returns:
            List of formatted cryptocurrency data
        """
        with open('assets/coinmarketcap-docs.txt', 'r') as f:
            return [f.read()]

    @server.resource("https://coinmarketcap.com/")
    def get_coinmarketcap_http_resource() -> list[str]:
        """
        Get cryptocurrency data.

        Returns:
            List of formatted cryptocurrency data
        """
        return ['https://coinmarketcap.com/']
