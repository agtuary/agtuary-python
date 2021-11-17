import requests


class HTTPClient(object):

    MAX_DELAY = 2
    INITIAL_DELAY = 0.5
    MAX_RETRY_AFTER = 60

    def __init__(self):
        pass

    def request(self, method, url, headers, post_data=None):

        if method == "get":
            response = requests.get(url, headers=headers)

            return response.json()
        elif method == "post":
            response = requests.post(url, headers=headers, data=post_data)

            return response.json()
