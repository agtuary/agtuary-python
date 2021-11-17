api_base = "http://127.0.0.1:3000"

from typing import List, Optional, Tuple, Union
import requests


from dataclasses import dataclass

from agtuary.api_resources.abstract.api_requestor import APIRequestor

from .rainfall_enums import ANNUAL, Seasons

from .api_resources import Analytics


class LocationDataError(Exception):
    pass


# a = Agtuary(...)
# a.analytics.get(...)
# a.rainfall() -> a.analytics.get()


class Agtuary(object):
    def __init__(
        self,
        email: str = "",
        password: str = "",
        endpoint: str = "https://api.agtuary.app",
    ):
        self._email = email
        self._password = password
        self.endpoint = endpoint
        self.key = self._login()
        self.requestor = APIRequestor(key=self.key, api_base=self.endpoint)

    def _login(self):
        api = APIRequestor(key="", api_base=self.endpoint)
        key = api.request(
            "post",
            "/v1/users/login",
            params={"email": self.email, "password": self.password},
        )["data"]["secret"]
        return key

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def analytics(self):
        return Analytics(self.requestor)

    # TODO
    # post to send geojosn and return p_id
    # get - give a p_id and return x
    # geo endpoint

    # @property
    # def rainfall_periods(self) -> List[str]:
    #     return [s.value for s in Seasons] + [ANNUAL]

    # @property
    # def rainfall_subtypes(self) -> List[str]:
    #     return ["volume", "consistency", "duration", "reliability"]

    # def rainfall(
    #     self,
    #     location: Union[Tuple[float, float], str],
    #     subtypes: Optional[List[str]] = None,
    #     periods: Optional[List[str]] = None,
    # ):
    #     url = "https://insert.url"
    #     headers = {"Authorization": f"Bearer {self.key}"}

    #     if not isinstance(subtypes, list):
    #         subtypes = self.rainfall_subtypes

    #     if not isinstance(periods, list):
    #         periods = self.rainfall_periods

    #     if isinstance(location, str):
    #         json = {"address": location, "point": {"latitude": None, "longitude": None}}
    #         return requests.post(url, headers=headers, json=json).json()
    #     elif (
    #         isinstance(location, tuple)
    #         and isinstance(location[0], float)
    #         and isinstance(location[1], float)
    #     ):
    #         point = {"latitude": location[0], "longitude": location[0]}
    #         json = {"address": None, "point": point}
    #         return requests.post(url, headers=headers, json=json).json()
    #     else:
    #         msg = "You must supply either an address string of a (lat, lon) tuple"
    #         raise LocationDataError(msg)
