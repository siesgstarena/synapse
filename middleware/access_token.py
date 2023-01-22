import os
from werkzeug.wrappers import Request, Response

# pylint: disable=too-few-public-methods


class VerifyAccessToken:
    def __init__(self, app):
        self.app = app
        self.access_token = os.environ.get("ACCESS_TOKEN")

    def __call__(self, environ, start_response):
        request = Request(environ)
        if request.path.startswith("/problem"):
            if request.headers.get("Authorization") != self.access_token:
                return Response("Unauthorized", status=401)(environ, start_response)

        return self.app(environ, start_response)
