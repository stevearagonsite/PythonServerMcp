from .base import BaseAppSettings
from pydantic_settings import SettingsConfigDict


class StagingAppSettings(BaseAppSettings):
    pass
    model_config = SettingsConfigDict(env_file=".staging.env")
