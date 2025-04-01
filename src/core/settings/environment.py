from enum import Enum

class Environment(str, Enum):
    LOCAL: str = "LOCAL"
    DEV: str = "DEVELOPMENT"
    STAGING: str = "STAGING"
    PROD: str = "PRODUCTION"
