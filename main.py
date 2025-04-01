#!/usr/bin/env python3

from src import main

if __name__ == "__main__":
    # Get the server instance
    server = main()
    # Run the MCP server
    server.run(transport="stdio")
