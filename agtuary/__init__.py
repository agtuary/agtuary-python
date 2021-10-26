from typing import List, Optional, Tuple, Union
import requests


from dataclasses import dataclass

from .rainfall_enums import ANNUAL, Seasons


class LocationDataError(Exception):
    pass


class Agtuary(object):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.key = None

    @property
    def periods(self) -> List[str]:
        return [s.value for s in Seasons] + [ANNUAL]

    @property
    def subtypes(self) -> List[str]:
        return ["volume", "consistency", "duration", "reliability"]

    def rainfall(
        self,
        location: Union[Tuple[float, float], str],
        subtypes: Optional[List[str]] = None,
        periods: Optional[List[str]] = None,
    ):
        url = "https://insert.url"
        headers = {"Authorization": f"Bearer {self.key}"}

        if not isinstance(subtypes, list):
            subtypes = self.subtypes

        if not isinstance(periods, list):
            periods = self.periods

        if isinstance(location, str):
            json = {"address": location, "point": {"latitude": None, "longitude": None}}
            return requests.post(url, headers=headers, json=json).json()
        elif (
            isinstance(location, tuple)
            and isinstance(location[0], float)
            and isinstance(location[1], float)
        ):
            point = {"latitude": location[0], "longitude": location[0]}
            json = {"address": None, "point": point}
            return requests.post(url, headers=headers, json=json).json()
        else:
            msg = "You must supply either an address string of a (lat, lon) tuple"
            raise LocationDataError(msg)
