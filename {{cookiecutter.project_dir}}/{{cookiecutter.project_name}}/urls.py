from django.conf import settings
from django.conf.urls import url, include
# Uncomment to enable i18n urls
#from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

from fluo import admin
#from django.contrib import admin

# Uncomment the next lines to enable custom handlers:
#from django.conf.urls import handler403, handler404, handler500
#handler403 = "{{ cookiecutter.project_name }}.views.handler403"
#handler404 = "{{ cookiecutter.project_name }}.views.handler404"
#handler500 = "{{ cookiecutter.project_name }}.views.handler500"

from django.views.generic import TemplateView
from django.views import i18n as i18n_views

urlpatterns = [
    url(r"^robots.txt", TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain",
    ), name="{{ cookiecutter.project_name }}-robots"),
    url(r"^crossdomain.xml$", TemplateView.as_view(
        template_name="crossdomain.xml",
        content_type="application/xml",
    ), name="{{ cookiecutter.project_name }}-crossdomain"),

    # Comment to disable i18n
    url(r"^i18n$", i18n_views.set_language, name="i18n"),
    url(r"^jsi18n$", i18n_views.javascript_catalog, name="jsi18n"),

    # Comment the next line to disable the admin:
    url(r"^admin/", include(admin.site.urls)),

    url(r"^$", TemplateView.as_view(template_name="index.html"), name="{{ cookiecutter.project_name }}-index"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Uncomment to enable i18n urls
#urlpatterns += i18n_patterns("",
    #url(r"^{{ cookiecutter.project_name }}/", include("{{ cookiecutter.project_name }}.foo.urls")),
#)
