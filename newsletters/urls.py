from django.conf.urls import url
from .views import join


urlpatterns = [
    url(r'^join/$', join, name='join'),
]
