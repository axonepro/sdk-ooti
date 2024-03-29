import json


class Resource:
    def __init__(
        self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination
    ):
        self.base_url = base_url
        self.org_pk = org_pk
        self.teams_pk = teams_pk
        self.access_token = access_token
        self._csrf_token = _csrf_token
        self.headers = headers
        self.pagination = pagination

    @staticmethod
    def process_response(response, results=None):
        """Process the response and return it

        :param: response is the response from the API
        :param: results is saying if we just want the results field of the response

        :return: {status, data} or {status} if data is not JSON serializable
        """
        try:
            if results is None:
                return {
                    "status": response.status_code,
                    "data": json.loads(response.content),
                }
            else:
                return {
                    "status": response.status_code,
                    "data": json.loads(response.content)["results"],
                }
        except ValueError:
            return {"status": response.status_code}
        except KeyError:
            return {
                "status": response.status_code,
                "data": json.loads(response.content),
            }

    @staticmethod
    def process_request(
        request, verb, _base_url, _route, _headers, _parameter=None, _data=None
    ):
        try:

            if verb == "GET":
                if _parameter is None:
                    return request.get(
                        f"{_base_url}{_route}", headers=_headers, data=_data
                    )
                else:
                    return request.get(
                        f"{_base_url}{_route}{_parameter}", headers=_headers, data=_data
                    )
            if verb == "POST":
                if _parameter is None:
                    return request.post(
                        f"{_base_url}{_route}", headers=_headers, data=_data
                    )
                else:
                    return request.post(
                        f"{_base_url}{_route}{_parameter}", headers=_headers, data=_data
                    )
            if verb == "PATCH":
                if _parameter is None:
                    return request.patch(
                        f"{_base_url}{_route}", headers=_headers, data=_data
                    )
                else:
                    return request.patch(
                        f"{_base_url}{_route}{_parameter}", headers=_headers, data=_data
                    )
            if verb == "DELETE":
                if _parameter is None:
                    return request.delete(
                        f"{_base_url}{_route}", headers=_headers, data=_data
                    )
                else:
                    return request.delete(
                        f"{_base_url}{_route}{_parameter}", headers=_headers, data=_data
                    )
            else:
                raise ValueError("Wrong verb! (", verb, ")")
        except ValueError as err:
            print("ValueError: ", err)
            return None
        except Exception as exc:
            print("Error: ", exc)
            return None
