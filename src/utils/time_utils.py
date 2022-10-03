from datetime import datetime, timedelta

import pytz


def now():
    return datetime.now(tz=pytz.timezone("US/Eastern"))


def stringify(datetime_object: datetime = now()) -> str:
    if datetime_object.tzinfo == "US/Eastern":
        return datetime_object.isoformat()
    raise ValueError("Invalid Time Zone")


def str2datetime(dateandtime: str) -> datetime:
    return datetime.strptime(dateandtime, "%Y-%m-%dT%H:%M:%S%z")


def timediff30(diff: datetime) -> bool:
    if diff < timedelta(30):
        return True
    else:
        return False
