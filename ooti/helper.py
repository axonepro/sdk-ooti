import json


class Helper:
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        self.base_url = base_url
        self.org_pk = org_pk
        self.teams_pk = teams_pk
        self.access_token = access_token
        self._csrf_token = _csrf_token
        self.headers = headers
        self.pagination = pagination

    def process_response(self, response, results=None):
        """ Process the response and return it

        :param: response is the response from the API
        :param: results is saying if we just want the results field of the response

        :return: {status, data} or {status} if data is not JSON serializable
        """
        try:
            if(results == None):
                return {'status': response.status_code, 'data': json.loads(response.content)}
            else:
                return {'status': response.status_code, 'data': json.loads(response.content)['results']}
        except ValueError:
            return {'status': response.status_code}
        except KeyError:
            return {'status': response.status_code, 'data': json.loads(response.content)}
