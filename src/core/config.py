from functools import lru_cache

from app.core.settings.base import BaseAppSettings

from .settings import (
    Environment,
    LocalAppSettings,
    DevelopmentAppSettings,
    StagingAppSettings,
    ProdAppSettings,
)

import decouple


env = decouple.config("ENVIRONMENT", default="DEV", cast=str)


class SettingsFactory:
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> BaseAppSettings:
        return {
            Environment.LOCAL: LocalAppSettings,
            Environment.DEV: DevelopmentAppSettings,
            Environment.STAGING: StagingAppSettings,
            Environment.PROD: ProdAppSettings,
        }.get(self.environment, LocalAppSettings)()


@lru_cache
def get_app_settings() -> BaseAppSettings:
    return SettingsFactory(environment=env)()


settings = get_app_settings()
