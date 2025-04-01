import logging
import os

# from pydantic import EmailStr, FieldValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from .environment import Environment


class BaseAppSettings(BaseSettings):
    ENVIRONMENT: Environment

    # APP PATH
    PROJECT_ROOT: str = os.path.abspath(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    )

    # DATE
    DEFAULT_LOCALE: str = "en_US"
    DATE_FORMAT: str = "%Y-%m-%d"
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"  # TODO add timezone

    # LOGS
    LOGGING_LEVEL: str = logging.getLevelName(logging.INFO)
    LOG_DIR: str = os.path.join(PROJECT_ROOT, "logs")  # TODO crear esta ruta
    ROTATION: str = "00:00"
    RETENTION: str = "7 days"

    # FIND QUERY
    PAGE: int = 1
    PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100
    ORDERING: str = "-created_at"

    # SALESFORCE
    SALESFORCE_USERNAME: str
    SALESFORCE_PASSWORD: str
    SALESFORCE_SECURITY_TOKEN: str
    ENVIRONMENT_SF: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        validate_assignment=True,
        extra="allow",
    )

    # CORS
    # ALLOWED_HOSTS: list[str] = ["localhost", "127.0.0.1"]
    # BACKEND_CORS_ORIGINS: list[str] = ["*"]
    # CORS_ORIGINS_REGEX: str | None = None

    # EMAIL
    # EMAILS_ENABLED: bool = False
    # EMAIL_TEMPLATES_DIR: str = os.path.join(PROJECT_ROOT, "core/templates")
    # EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48

    # EMAILS_FROM_NAME: str | None = None
    # EMAILS_FROM_EMAIL: EmailStr | None = None
    # EMAILS_FROM: str | None = None
    # EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore

    # @field_validator("EMAILS_FROM")
    # @classmethod
    # def get_emaixl_from(cls, v: str | None, info: FieldValidationInfo) -> str:
    #     if not v:
    #         return f"{info.data['EMAILS_FROM_NAME']} <{info.data['EMAILS_FROM_EMAIL']}>"
    #     return v

    # RESEND_API_KEY: str

    # DATABASE
    # POSTGRES_USER: str
    # POSTGRES_PASSWORD: str
    # POSTGRES_SERVER: str
    # POSTGRES_PORT: int
    # POSTGRES_DB: str
    # SQLALCHEMY_DATABASE_URI: str | None = None
    # SQLALCHEMY_DATABASE_ASYNC_URI: str | None = None

    # @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    # @classmethod
    # def assemble_db_connection(cls, v: str, values: FieldValidationInfo):
    #     return f'postgresql://{values.data.get("POSTGRES_USER")}:{values.data.get("POSTGRES_PASSWORD")}@{values.data.get("POSTGRES_SERVER")}:{values.data.get("POSTGRES_PORT")}/{values.data.get("POSTGRES_DB")}'

    # @field_validator("SQLALCHEMY_DATABASE_ASYNC_URI", mode="before")
    # @classmethod
    # def assemble_async_db_connection(cls, v: str, values: FieldValidationInfo):
    #     return f'postgresql+asyncpg://{values.data.get("POSTGRES_USER")}:{values.data.get("POSTGRES_PASSWORD")}@{values.data.get("POSTGRES_SERVER")}:{values.data.get("POSTGRES_PORT")}/{values.data.get("POSTGRES_DB")}'

    # MAX_CONNECTION_COUNT: int = 10
    # MIN_CONNECTION_COUNT: int = 10
    # SQLALCHEMY_ECHO: bool = False

    # @property
    # def SQLALCHEMY_ENGINE_OPTIONS(self) -> dict[str, any]:
    #     return {
    #         "pool_size": 10,
    #         "max_overflow": 20,
    #         "pool_pre_ping": True,
    #         "echo": self.SQLALCHEMY_ECHO,
    #         "connect_args": {"options": "-c timezone=Etc/GMT+6"}
    #         # 'encoding': "utf-8",
    #         # 'pool_recycle': 1800,
    #         # 'convert_unicode': True,
    #     }

    # REDIS
    # REDIS_SERVER: str
    # REDIS_PORT: int
    # REDIS_PASSWORD: str
    # REDIS_DB: int
