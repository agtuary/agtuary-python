from dataclasses import dataclass
from typing import List, Optional, Union
from numbers import Number
from endpoint import Data, V1Endpoint


@dataclass
class AnalyticsData:
    id: str
    product: str
    subtype: str
    name: str
    description: str
    values: list

    team: str
    project: str
    region: str
    user: str

    summary: Optional[str] = None
    dotpoints: Optional[list] = None
    table: Optional[dict] = None
    score: Optional[dict] = None

    across: Optional[str] = None
    created: Optional[str] = None
    updated: Optional[str] = None
    interval: Optional[List[Union[int, str]]] = None
    anchor: Optional[str] = None
    points: Optional[Number] = None
    calculated_description: Optional[str] = None
    score_description: Optional[str] = None

    def __init__(self, data):
        self.json = data

    def __getitem__(self, key):
        v = [j for j in self.json if j["product"] == key or j["subtype"] == key]
        return v

    def __iter__(self):
        return iter(self.json)

    def __len__(self):
        return len(self.json)

    def as_dataframe(self):
        import pandas as pd

        pass

    def as_array(self):
        pass


class Analytics(V1Endpoint):
    COLLECTION_NAME = "analytics"

    def get(self, id: Optional[str] = None):

        url = self.url + f"/{id}" if isinstance(id, str) else self.url
        response = self.requestor.request("get", url)
        anal_list = [
            AnalyticsData(**a) for a in super().check_error(response).json_array
        ]
        return anal_list
