from dataclasses import dataclass


class RequestMethod(object):
    METHOD = None


class RequestPOST(RequestMethod):
    METHOD = 'post'


class RequestGET(RequestMethod):
    METHOD = 'get'


@dataclass
class RequestMethods(object):
    POST = RequestPOST()
    GET = RequestGET()
