import requests
import json

from helper import Helper


class Others(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers):
        self.base_url = base_url
        self.org_pk = org_pk
        self.teams_pk = teams_pk
        self.access_token = access_token
        self._csrf_token = _csrf_token
        self.headers = headers

    #### Goals ####

    #### Help ####

    #### Indicators ####

    #### Pipelines ####

    #### Projections ####
