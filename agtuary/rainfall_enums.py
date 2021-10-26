from enum import Enum

ANNUAL = "annual"


class Seasons(Enum):
    SUMMER = "summer"
    AUTUMN = "autumn"
    WINTER = "winter"
    SPRING = "spring"


months = {
    Seasons.SUMMER: [12, 1, 2],
    Seasons.AUTUMN: [3, 4, 5],
    Seasons.WINTER: [6, 7, 8],
    Seasons.SPRING: [9, 10, 11],
}
