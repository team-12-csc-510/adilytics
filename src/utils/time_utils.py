import calendar
from datetime import date, datetime,timedelta

import pytz  # type:ignore


def now():
    return datetime.now(tz=pytz.timezone("US/Eastern"))


def stringify(datetime_object: datetime = now()) -> str:
    if datetime_object.tzinfo == "US/Eastern":
        return datetime_object.isoformat()
    raise ValueError("Invalid Time Zone")


def str2datetime(dateandtime: str) -> datetime:
    return datetime.strptime(dateandtime, "%Y-%m-%dT%H:%M:%S%z")


def timediff30(diff: timedelta) -> bool:
    if diff < timedelta(30):
        return True
    else:
        return False


def get_start_month_date(months: int) -> date:
    currentDate = datetime.today()
    firstDayOfMonth = date(currentDate.year, currentDate.month - months, 1)
    return firstDayOfMonth


def get_end_month_date(months: int) -> date:
    currentDate = datetime.today()
    lastDayOfMonth = date(
        currentDate.year,
        currentDate.month - months,
        calendar.monthrange(currentDate.year, currentDate.month - months)[1],
    )
    return lastDayOfMonth
