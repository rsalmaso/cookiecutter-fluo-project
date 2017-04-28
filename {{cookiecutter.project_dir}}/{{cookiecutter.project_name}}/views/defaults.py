from django.views import defaults as default_views
from django.views.decorators.csrf import requires_csrf_token


@requires_csrf_token
def bad_request(request, exception, template_name="400.html"):
    return default_views.bad_request(request, exception, template_name)


@requires_csrf_token
def permission_denied(request, exception, template_name="403.html"):
    return default_views.permission_denied(request, exception, template_name)


@requires_csrf_token
def page_not_found(request, exception, template_name="404.html"):
    return default_views.page_not_found(request, exception, template_name)


@requires_csrf_token
def server_error(request, template_name="500.html"):
    return default_views.server_error(request, template_name)
