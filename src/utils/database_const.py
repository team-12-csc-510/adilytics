from enum import Enum, auto


class Databases(Enum):
    """
    Defines database with their name and numbers
    """

    adilytics = auto()


class Collections(Enum):
    """
    Defines collections with their name and numbers
    """

    users = auto()
    analytics = auto()
    ad = auto()
    click = auto()
    company = auto()
    location = auto()
    product = auto()
