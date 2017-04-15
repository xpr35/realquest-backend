from django.http import HttpResponse
from django.conf import settings


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if 'HTTP_X_AUTH_TOKEN' in request.META:
            if settings.AUTH_TOKEN == request.META['HTTP_X_AUTH_TOKEN']:
                return self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return HttpResponse('Unauthorized', status=401)

