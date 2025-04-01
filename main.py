import mcp
from mcp.server import Server
from mcp.tools import Tool


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
    server = Server(name="crypto-price-server")

    # Register tools
    server.register_tool(
        Tool(
            name="get_crypto_price",
            function=get_crypto_price,
            description="Get the current price of a cryptocurrency",
        )
    )

    return server


if __name__ == "__main__":
    mcp.run(transport="stdio")
