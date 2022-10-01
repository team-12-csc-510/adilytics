from enum import Enum, auto


class Databases(Enum):
    adilytics = auto()


class Collections(Enum):
    users = auto()
    analytics = auto()
    ad = auto()
    click = auto()
    company = auto()
    location = auto()
    product = auto()
