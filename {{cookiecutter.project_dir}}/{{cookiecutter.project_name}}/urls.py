from django.conf import settings{% if cookiecutter.project_type == "django-cms" %}
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns{% else %}
from django.urls import include, re_path as url
# Uncomment to enable i18n urls
#from django.conf.urls.i18n import i18n_patterns{% endif %}
from django.conf.urls.static import static
from django.views import i18n as i18n_views
from django.views.generic import TemplateView
from fluo import admin

from . import views

handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.server_error

catalog_patterns = [
    url(r"^plain$", i18n_views.set_language, name="i18n"),
    url(r"^javascript/(?P<packages>\S+?)$", i18n_views.JavaScriptCatalog.as_view(), name="js"),
    url(r"^json/(?P<packages>\S+?)$", i18n_views.JSONCatalog.as_view(), name="json"),
]

urlpatterns = [
    url(r"^robots\.txt", TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain",
    ), name="{{ cookiecutter.project_name }}-robots"),
    url(r"^crossdomain\.xml$", TemplateView.as_view(
        template_name="crossdomain.xml",
        content_type="application/xml",
    ), name="{{ cookiecutter.project_name }}-crossdomain"),

    url(r"^i18n/", include((catalog_patterns, "i18n"))),{% if cookiecutter.project_type != "django-cms" %}

    url(r"^admin/", admin.site.urls),

    url(r"^$", TemplateView.as_view(template_name="{{ cookiecutter.project_name }}/index.html"), name="{{ cookiecutter.project_name }}-index"),{% endif %}
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400$', views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403$', views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404$', views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500$', views.server_error),
    ]


{% if cookiecutter.project_type == "django-cms" %}urlpatterns += i18n_patterns(
    url(r"^admin/", admin.site.urls),
    url(r"^", include("cms.urls")),
){% else %}
#urlpatterns += i18n_patterns(
    #url(r"^{{ cookiecutter.project_name }}/", include("{{ cookiecutter.project_name }}.foo.urls")),
#){% endif %}
