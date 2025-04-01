from .base import BaseAppSettings
from pydantic import SettingsConfigDict


class StagingAppSettings(BaseAppSettings):
    pass
    model_config = SettingsConfigDict(env_file=".prod.env")
