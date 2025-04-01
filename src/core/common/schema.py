import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from src.app.utilities.datetime import custom_datetime


class OrmBaseModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        populate_by_name=True,
        json_encoders={datetime.datetime: custom_datetime},
    )


class TimestampModelMixin(OrmBaseModel):
    created_at: datetime.datetime
    updated_at: datetime.datetime | None


class UUIDModelMixin(OrmBaseModel):
    id: UUID


class StringModelMixin(OrmBaseModel):
    id: str


class StringTagModelMixin(OrmBaseModel):
    tag: str


class IntegerIDModelMixin(OrmBaseModel):
    id: int
