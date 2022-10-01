from datetime import datetime

import pytz


def now():
    return datetime.now(tz=pytz.timezone("US/Eastern"))


def stringify(datetime_object: datetime = now()) -> str:
    if datetime_object.tzinfo == "US/Eastern":
        return datetime_object.isoformat()
    raise ValueError("Invalid Time Zone")
