# act_project/act/act/urls.py
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from .admin import admin_site
from .views_api import api_root

handler400 = 'website.views.handler400'
handler403 = 'website.views.handler403'
handler404 = 'website.views.handler404'
handler500 = 'website.views.handler500'

urlpatterns = [
    url(r'^deus_ex_machina/', admin_site.urls),
]

''' Internationalization '''

urlpatterns += i18n_patterns(
    url(r'', include('website.urls')),
    prefix_default_language=False
)

''' Root API view '''

urlpatterns += [
    url(r'^api/$', api_root),
]

''' Metadata application API '''

urlpatterns += [
    url(r'^api/', include('metadata.urls_api')),
]

''' Subscription application API '''

urlpatterns += [
    url(r'^api/', include('subscription.urls_api')),
]

''' Website application API '''

urlpatterns += [
    url(r'^api/', include('website.urls_api')),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)