"""System resources for the MCP server.

Reference: https://coinmarketcap.com/
"""

import logging
import os
from pathlib import Path

# Configure logging
logger = logging.getLogger(__name__)


def register_resources(server):
    """Register all system resources with the server.

    Args:
        server: MCP server instance
    """

    @server.resource(
        "template://assets/{folder}/{file}",
        description="resource template",
    )
    def get_file_docs(
        folder: str = "docs", file: str = "coinmarketcap-docs.txt"
    ) -> str:
        """Get cryptocurrency data.

        Returns:
            Formatted cryptocurrency data
        """
        project_root = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent
        file_path = os.path.join(project_root, "assets", folder, file)
        with open(file_path, "r") as f:
            return f.read()

    @server.resource("https://coinmarketcap.com/")
    def get_coinmarketcap_http_resource() -> str:
        """Get cryptocurrency data.

        Returns:
            Formatted cryptocurrency data
        """
        return "https://coinmarketcap.com/"
