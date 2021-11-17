from ..abstract.api_requestor import APIRequestor
from dataclasses import dataclass


@dataclass
class Data(object):
    json_array: list


class V1Endpoint(object):
    def __init__(self, requestor: APIRequestor):
        self.requestor = requestor

    @property
    def url(self):
        return f"/v1/{self.COLLECTION_NAME}"

    def check_error(self, response):
        if not response["error"]:
            return Data(json_array=response["data"])

        raise Exception(response["error"]["description"], response["error"]["code"])
