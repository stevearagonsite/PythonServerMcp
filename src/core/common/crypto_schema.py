from pydantic import BaseModel, Field
from typing import Optional


class CryptoCurrency(BaseModel):
    """Schema for cryptocurrency data"""
    symbol: str
    name: str
    price: float
    percent_change_24h: Optional[float] = None
    market_cap: Optional[float] = None
    volume_24h: Optional[float] = None
    last_updated: Optional[str] = None


class CryptoResponse(BaseModel):
    """Schema for API response"""
    status: str = Field(default="success")
    data: CryptoCurrency
