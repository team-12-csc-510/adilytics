from datetime import datetime, timedelta

import pytz  # type:ignore


def now():
    return datetime.now(tz=pytz.timezone("US/Eastern"))


def stringify(datetime_object: datetime = now()) -> str:
    if datetime_object.tzinfo == "US/Eastern":
        return datetime_object.isoformat()
    raise ValueError("Invalid Time Zone")


def time_now() -> datetime:
    return datetime.now()


def timediff30(diff: datetime) -> timedelta:
    return diff - timedelta(days=30)
