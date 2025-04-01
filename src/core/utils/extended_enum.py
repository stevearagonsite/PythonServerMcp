from enum import Enum
from src.app.core.exceptions import exception


class ExtendedEnum(str, Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def list_of_dict(cls):
        return [{"name": item} for item in cls.list()]

    @classmethod
    def auto_num(cls):
        return {item: i for i, item in enumerate(cls.list())}


class StatusEnum(ExtendedEnum):

    def transitions(self) -> list["StatusEnum"]:
        raise NotImplementedError()

    def validate_transition(self, new_status: "StatusEnum"):
        if not new_status in self.transitions():
            raise exception.BadRequestException(f"Invalid transition from {self} to {new_status}")
