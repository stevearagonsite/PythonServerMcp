from .base import BaseAppSettings
from pydantic_settings import SettingsConfigDict


class ProductionAppSettings(BaseAppSettings):
    pass
    model_config = SettingsConfigDict(env_file=".prod.env")
