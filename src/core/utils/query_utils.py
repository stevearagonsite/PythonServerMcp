# https://gist.github.com/ghandic/21c27470f6797dd856208a2c68f3e43a
from pydantic import BaseModel
from fastapi import Query
from src.app.utilities.extended_enum import ExtendedEnum
from src.app.core.exceptions import exception
from enum import EnumMeta


class SortOption(ExtendedEnum):
    asc = "asc"
    desc = "desc"


# @extend_enum()
class QuerySortEnum(ExtendedEnum):
    @property
    def field(self) -> str:
        if self.value[0] == "-":
            return self.value[1:]
        return self.value

    @property
    def by(self) -> SortOption:
        if self.value[0] == "-":
            return SortOption.desc
        return SortOption.asc


def extend_enum():
    def wrapper(added_enum: EnumMeta):
        joined = {}
        for item in added_enum:
            joined[item.name] = item.value
            joined[f"{item.name}_"] = f"-{item.value}"
        return QuerySortEnum(added_enum.__name__, joined)

    return wrapper


class SortBy(BaseModel):
    name: str
    by: SortOption

    # @staticmethod
    # def create(options: list[str]) -> str:
    #     return "|".join(f"^{opt}$|^-{opt}$" for opt in options)

    @staticmethod
    def parse(value: str) -> "SortBy":
        sort_option = SortOption.asc
        if value[0] == "-":
            value = value[1:]
            sort_option = SortOption.desc
        return SortBy(name=value, by=sort_option)


class Sorts(BaseModel):
    sort: list[SortBy] | None = None

    # @staticmethod
    # def create(options: list[str]) -> str:
    #     return r"-?\w+,?"

    @staticmethod
    def parse(values: list[str]) -> "Sorts":
        response = []
        for value in values:
            sort_option = SortOption.asc
            if value[0] == "-":
                value = value[1:]
                sort_option = SortOption.desc
            response.append(SortBy(name=value, by=sort_option))
        return response


def parse_sort(options: list[str]):
    async def _parse_sort(sort: list[str] = Query(None, description=f"Allowed values: {options}")):
        if sort:
            if not set([s.replace("-", "") for s in sort]).issubset(set(options)):
                raise exception.BaseAPIError(status_code=422, detail=f"Invalid sort options. Allowed values: {options}")
            return Sorts.parse(sort)

    return _parse_sort
