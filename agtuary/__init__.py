import requests


class Agtuary(object):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
