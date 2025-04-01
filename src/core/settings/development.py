from .base import BaseAppSettings
from pydantic import SettingsConfigDict


class DevelopmentAppSettings(BaseAppSettings):
    pass
    model_config = SettingsConfigDict(env_file=".dev.env")
