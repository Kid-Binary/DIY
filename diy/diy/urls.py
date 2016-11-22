# diy_project/diy/diy/urls.py
from django.conf.urls import include, url
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

from django.contrib import admin

from .admin import admin_site

handler400 = 'website.views.handler400'
handler403 = 'website.views.handler403'
handler404 = 'website.views.handler404'
handler500 = 'website.views.handler500'

urlpatterns = [
    url(r'^deus_ex_machina/', admin_site.urls),
    url(r'^nested_admin/', include('nested_admin.urls')),
]

urlpatterns += i18n_patterns(
    url(r'', include('website.urls')),
    prefix_default_language=False
)

''' API: website app '''

urlpatterns += [
    url(r'^api/', include('website.urls_api', namespace='website_api')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)