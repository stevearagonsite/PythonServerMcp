"""Tools package for the MCP server."""

from . import prices


def register_all_tools(server):
    """
    Register all tools with the server.

    Args:
        server: MCP server instance
    """
    prices.register_tools(server)
