# act_project/act/website/urls.py
from django.conf.urls import url

from . import views

app_name = 'website'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?:.*)/?$', views.index, name='react'),
]
