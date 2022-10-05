from datetime import datetime

import pytz  # type:ignore


def now():
    """
    Function to get the current Eastern Time
    :return: datetime object of current eastern time
    """
    return datetime.now(tz=pytz.timezone("US/Eastern"))


def stringify(datetime_object: datetime = now()) -> str:
    """
    Convert datetime object to string
    :param datetime_object: datetime object
    :return: datetime in string in isoformat
    """
    if datetime_object.tzinfo == "US/Eastern":
        return datetime_object.isoformat()
    raise ValueError("Invalid Time Zone")
