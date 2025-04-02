"""Resources package for the MCP server."""

from . import coinmarketcap_resource


def register_all_resources(server):
    """
    Register all resources with the server.

    Args:
        server: MCP server instance
    """
    coinmarketcap_resource.register_resources(server)
