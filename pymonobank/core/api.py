import requests

from pymonobank.request import RequestPOST, RequestGET, exceptions


class MonoApi(object):
    BASE_URL = 'https://api.monobank.ua'
    AUTH_HEADER = 'X-Token'
    TOKEN = None

    def __init__(self, token: str):
        self.TOKEN = token

    @staticmethod
    def post(
            url: str,
            data: dict,
            headers: dict = None
    ) -> requests.Response:
        """
        Sends a POST request through the requests.post method and returns a response to the server.

        Throws errors:
            * TypeError: if any parameter does not match the correct type

        :param url: string, request url
        :param data: dict, request data
        :param headers: dict, request headers
        :return: requests.Response
        """

        if not isinstance(url, str):
            raise TypeError(f'url arg must be str not `{type(url)}`')

        if headers and not isinstance(headers, dict):
            raise TypeError(f'headers arg must be dict not `{type(headers)}`')

        if not isinstance(data, dict):
            raise TypeError(f'data arg must be dict not `{type(data)}`')

        return requests.post(
            url=url,
            json=data,
            headers=headers
        )

    @staticmethod
    def get(
            url: str,
            params: dict = None,
            headers: dict = None
    ) -> requests.Response:
        """
        Sends a GET request through the requests.get method and returns a response to the server.

        Throws errors:
            * TypeError: if any parameter does not match the correct type

        :param url: string, request url
        :param params: dict, request params
        :param headers: dict, request headers
        :return: requests.Response
        """

        if not isinstance(url, str):
            raise TypeError(f'url arg must be str not `{type(url)}`')

        if params and not isinstance(params, dict):
            raise TypeError(f'params arg must be dict not `{type(params)}`')

        if headers and not isinstance(headers, dict):
            raise TypeError(f'headers arg must be dict not `{type(headers)}`')

        return requests.get(
            url=url,
            params=params,
            headers=headers
        )

    def request(
            self,
            url: str,
            method: RequestPOST | RequestGET,
            data: dict = None,
            params: dict = None,
            headers: dict = None
    ) -> requests.Response:
        """
        Sends a request to the server depending on the method and url and returns a response to the server.

        Throws errors:
            * TypeError: if any parameter does not match the correct type
            * RequestMethodNotFoundError: if the method parameter does not match the available class object

        :param url: string, request url
        :param method: instance of RequestPOST or RequestGET classes
        :param data: dict, request data with POST request
        :param params: dict, request data with GET request
        :param headers: dict, request headers
        :return: requests.Response
        """

        request_headers = {self.AUTH_HEADER: self.TOKEN}

        if headers:
            if not isinstance(headers, dict):
                raise TypeError(f'headers arg must be dict not `{type(headers)}`')
            request_headers = {**request_headers, **headers}

        if isinstance(method, RequestPOST):
            return self.post(url=url, data=data, headers=request_headers)
        elif isinstance(method, RequestGET):
            return self.get(url=url, params=params, headers=request_headers)
        else:
            raise exceptions.RequestMethodNotFoundError(f'method {method} not found to processing')
