"""System tools for the MCP server."""

import json
import logging

from src.core.common.crypto_schema import CryptoCurrency, CryptoResponse
from src.services import get_cryptocurrency_data

# Configure logging
logger = logging.getLogger(__name__)


def register_tools(server):
    """
    Register all system tools with the server.

    Args:
        server: MCP server instance
    """

    @server.tool()
    async def get_crypto_price(symbol: str) -> str:
        """
        Get the current price of a cryptocurrency using CoinMarketCap API.

        Args:
            symbol: The symbol of the cryptocurrency (e.g., BTC, ETH)

        Returns:
            JSON string with cryptocurrency data or error message
        """
        # Convert symbol to uppercase
        symbol = symbol.upper()

        try:
            # Get data from CoinMarketCap API
            crypto_data = get_cryptocurrency_data(symbol)

            if crypto_data:
                # Create response with the data
                response = CryptoResponse(status="success", data=crypto_data)
                return json.dumps(response.model_dump(), default=str)
            else:
                # If API call failed or data not found, return error
                fallback_data = CryptoCurrency(
                    symbol=symbol, name=f"{symbol} Coin", price=0.0, last_updated="N/A"
                )
                response = CryptoResponse(status="error", data=fallback_data)
                return json.dumps(response.model_dump(), default=str)
        except Exception as e:
            logger.error(f"Error getting price for {symbol}: {e}")
            # Return error message
            return json.dumps(
                {
                    "status": "error",
                    "message": f"Failed to get price for {symbol}: {str(e)}",
                }
            )
