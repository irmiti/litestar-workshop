from litestar.connection import ASGIConnection
from litestar.exceptions import NotAuthorizedException
from litestar.handlers import BaseRouteHandler


def api_key_guard(connection: ASGIConnection, _: BaseRouteHandler) -> None:
    """ @:param: connection: ASGIConnection is the Request or WebSocket instance
    (both are subclasses of ASGIConnection)
    """
    if "X-API-KEY" not in connection.headers:
        raise NotAuthorizedException