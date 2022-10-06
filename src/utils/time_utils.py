from datetime import datetime

import pytz  # type:ignore


def now():
    """Function to return the current date time

    :return: Returns the current datetime in US/Eastern timezone
    """
    return datetime.now(tz=pytz.timezone("US/Eastern"))


def stringify(datetime_object: datetime = now()) -> str:
    if datetime_object.tzinfo == "US/Eastern":
        return datetime_object.isoformat()
    raise ValueError("Invalid Time Zone")
