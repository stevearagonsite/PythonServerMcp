from .base import BaseAppSettings
from pydantic_settings import SettingsConfigDict


class DevelopmentAppSettings(BaseAppSettings):
    pass
    model_config = SettingsConfigDict(env_file=".dev.env")
