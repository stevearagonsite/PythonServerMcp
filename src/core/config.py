from functools import lru_cache

from src.core.settings.base import BaseAppSettings

from src.core.settings import (
    Environment,
    LocalAppSettings,
    DevelopmentAppSettings,
    StagingAppSettings,
    ProductionAppSettings,
)

import decouple


env = decouple.config("ENVIRONMENT", default="DEV", cast=str)


class SettingsFactory:
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> BaseAppSettings:
        # Handle both PROD and PRODUCTION for production environment
        if self.environment in [Environment.PROD, "PRODUCTION"]:
            return ProductionAppSettings()
        
        return {
            Environment.LOCAL: LocalAppSettings,
            Environment.DEV: DevelopmentAppSettings,
            Environment.STAGING: StagingAppSettings,
        }.get(self.environment, LocalAppSettings)()


@lru_cache
def get_app_settings() -> BaseAppSettings:
    return SettingsFactory(environment=env)()


settings = get_app_settings()
