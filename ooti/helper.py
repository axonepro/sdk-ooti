import json


class Helper(object):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super(Helper, self).__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

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
