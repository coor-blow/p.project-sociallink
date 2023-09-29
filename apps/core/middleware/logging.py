from apps.landing.logging import Logging
from config.settings.base import BASE_DIR
import logging
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


logger = logging.getLogger('logging_mw')


def simple_logging_middleware(get_response):
    def middleware(request):
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers['Content-Type']
        user_agent = request.headers['User-Agent']
        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"

        logger.info(msg)

        response = get_response(request)

        return response
    return middleware


class ViewExecutionTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = timezone.now()

        response = self.get_response(request)

        total_time = timezone.now() - start_time

        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()

        msg = f" EXECUTION TIME 2  {total_time} >> {http_method} | {host_port}{url}"

        logger.info(msg)

        return response