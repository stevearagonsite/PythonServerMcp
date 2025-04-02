import requests
import logging
from typing import Optional

from src.core.common.crypto_schema import CryptoCurrency
from src.core.config import settings

logger = logging.getLogger(__name__)

def get_cryptocurrency_data(symbol: str) -> Optional[CryptoCurrency]:
    """
    Get cryptocurrency data from CoinMarketCap API
    
    Args:
        symbol: The symbol of the cryptocurrency (e.g., BTC, ETH)
        
    Returns:
        CryptoCurrency object with the data or None if there was an error
    """
    if not settings.COINMARKETCAP_API_KEY:
        logger.warning("CoinMarketCap API key not configured")
        return None
        
    url = f"{settings.COINMARKETCAP_API_URL}/cryptocurrency/quotes/latest"
    
    headers = {
        "X-CMC_PRO_API_KEY": settings.COINMARKETCAP_API_KEY,
        "Accept": "application/json"
    }
    
    params = {
        "symbol": symbol,
        "convert": "USD"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if "data" in data and symbol in data["data"]:
            crypto_data = data["data"][symbol]
            quote = crypto_data.get("quote", {}).get("USD", {})
            
            return CryptoCurrency(
                symbol=symbol,
                name=crypto_data.get("name", "Unknown"),
                price=quote.get("price", 0.0),
                percent_change_24h=quote.get("percent_change_24h"),
                market_cap=quote.get("market_cap"),
                volume_24h=quote.get("volume_24h"),
                last_updated=quote.get("last_updated")
            )
        
        logger.error(f"Failed to get data for {symbol}: {data.get('status', {}).get('error_message', 'Unknown error')}")
        return None
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making request to CoinMarketCap API: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error processing cryptocurrency data: {e}")
        return None
