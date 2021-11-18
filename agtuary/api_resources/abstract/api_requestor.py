import calendar
import time
import datetime
from collections import OrderedDict

from urllib.parse import urlencode

from agtuary.http_client import HTTPClient
import agtuary


def _encode_datetime(dttime):
    if dttime.tzinfo and dttime.tzinfo.utcoffset(dttime) is not None:
        utc_timestamp = calendar.timegm(dttime.utctimetuple())
    else:
        utc_timestamp = time.mktime(dttime.timetuple())

    return int(utc_timestamp)


def _encode_nested_dict(key, data, fmt="%s[%s]"):
    d = OrderedDict()
    for subkey, subvalue in data.items():
        d[fmt % (key, subkey)] = subvalue
    return d


def _api_encode(data):
    for key, value in data.items():
        if value is None:
            continue
        elif hasattr(value, "stripe_id"):
            yield (key, value.stripe_id)
        elif isinstance(value, list) or isinstance(value, tuple):
            for i, sv in enumerate(value):
                if isinstance(sv, dict):
                    subdict = _encode_nested_dict("%s[%d]" % (key, i), sv)
                    for k, v in _api_encode(subdict):
                        yield (k, v)
                else:
                    yield ("%s[%d]" % (key, i), sv)
        elif isinstance(value, dict):
            subdict = _encode_nested_dict(key, value)
            for subkey, subvalue in _api_encode(subdict):
                yield (subkey, subvalue)
        elif isinstance(value, datetime.datetime):
            yield (key, _encode_datetime(value))
        else:
            yield (key, value)


class APIRequestor(object):
    def __init__(self, key=None, api_base=None):
        self.api_key = key
        self.api_base = api_base
        self.client = HTTPClient()

    def request(self, method, url, params=None, headers=None):
        return self.request_raw(method, url, params, headers)

    def request_raw(self, method, url, params=None, supplied_headers=None):

        if self.api_key is None:
            raise TypeError("api_key must not be None")

        abs_url = "%s%s" % (self.api_base, url)

        encoded_params = urlencode(list(_api_encode(params or {})))

        if method == "get":
            if params:
                abs_url = "%s/%s" % (abs_url, encoded_params)
            post_data = None

        elif method == "post":
            post_data = encoded_params
        else:
            raise ValueError("method must either be get or post")

        headers = self.request_headers(self.api_key, method)

        if supplied_headers is not None:
            for key, value in supplied_headers.items():
                headers[key] = value

        return self.client.request(method, abs_url, headers, post_data=post_data)

    def request_headers(self, api_key, method):

        headers = {"Authorization": "Bearer %s" % (api_key)}

        if method == "post":
            headers["Content-Type"] = "application/x-www-form-urlencoded"

        return headers
