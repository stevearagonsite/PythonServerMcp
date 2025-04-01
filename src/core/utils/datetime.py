import json
import pytz
from datetime import date, time, datetime

from src.app.core.config.manager import settings


DEFAULT_TIMEZONE = pytz.timezone(settings.TIMEZONE)
ARG_TZ = pytz.timezone("America/Argentina/Buenos_Aires")


def aware_timezone(dt: datetime) -> datetime:
    return dt.replace(tzinfo=ARG_TZ)


def custom_datetime(dt: datetime) -> datetime:
    if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
        dt = aware_timezone(dt)
    return dt.replace(microsecond=0).astimezone(ARG_TZ).isoformat()


def transform_date_to_datetime(d: date, tz):
    dt = datetime.combine(d, time(0, 0, 0))
    dt = tz.localize(dt)
    return dt


def get_timestamp():
    ct = datetime.now()
    return ct.timestamp()

def start_of_day(day: datetime | date = datetime.now())->datetime:
    if isinstance(day, datetime): 
        return day.replace(hour=0, minute=0, second=0, microsecond=0)
    else: 
        return datetime(day.year, day.month, day.day, 0, 0, 0, 0)
    
def end_of_day(day: datetime | date = datetime.now())->datetime:
    if isinstance(day, datetime): 
        return day.replace(hour=23, minute=59, second=59, microsecond=0)
    else: 
        return datetime(day.year, day.month, day.day, 23, 59, 59, 0)
