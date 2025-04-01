from mcp.server.fastmcp import FastMCP


def get_crypto_price(symbol: str) -> str:
    """
    Get the current price of a cryptocurrency.

    Args:
        symbol: The symbol of the cryptocurrency (e.g., BTC, ETH)

    Returns:
        The current price of the cryptocurrency
    """
    # This is a placeholder - we'll implement the actual API call later
    return f"Price of {symbol}: $30,000 USD (placeholder)"


def main():
    # Create a FastMCP server instance
    server = FastMCP(name="crypto-price-server")

    # Add the get_crypto_price tool
    server.add_tool(
        name="get_crypto_price",
        fn=get_crypto_price,
        description="Get the current price of a cryptocurrency",
    )

    return server


if __name__ == "__main__":
    server = main()
    server.run(transport="stdio")
