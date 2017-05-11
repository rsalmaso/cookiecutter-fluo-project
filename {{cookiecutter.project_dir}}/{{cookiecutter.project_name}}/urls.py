from django.conf import settings
from django.conf.urls import url, include{% if cookiecutter.project_type == "django-cms" %}
from django.conf.urls.i18n import i18n_patterns{% else %}
# Uncomment to enable i18n urls
#from django.conf.urls.i18n import i18n_patterns{% endif %}
from django.conf.urls.static import static
from fluo import admin

handler400 = "{{ cookiecutter.project_name }}.views.bad_request"
handler403 = "{{ cookiecutter.project_name }}.views.permission_denied"
handler404 = "{{ cookiecutter.project_name }}.views.page_not_found"
handler500 = "{{ cookiecutter.project_name }}.views.server_error"

from django.views.generic import TemplateView
from django.views import i18n as i18n_views
from . import views

catalog_patterns = [
    url(r"^plain$", i18n_views.set_language, name="i18n"),
    url(r"^javascript/(?P<packages>\S+?)$", i18n_views.javascript_catalog, name="js"),
    url(r"^json/(?P<packages>\S+?)$", i18n_views.json_catalog, name="json"),
]

urlpatterns = [
    url(r"^robots.txt", TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain",
    ), name="{{ cookiecutter.project_name }}-robots"),
    url(r"^crossdomain.xml$", TemplateView.as_view(
        template_name="crossdomain.xml",
        content_type="application/xml",
    ), name="{{ cookiecutter.project_name }}-crossdomain"),

    url(r"^i18n/", include(catalog_patterns, namespace="i18n")),{% if cookiecutter.project_type != "django-cms" %}

    url(r"^admin/", include(admin.site.urls)),

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
    url(r"^admin/", include(admin.site.urls)),
    url(r"^", include("cms.urls")),
){% else %}
#urlpatterns += i18n_patterns(
    #url(r"^{{ cookiecutter.project_name }}/", include("{{ cookiecutter.project_name }}.foo.urls")),
#){% endif %}
