from django.conf.urls import url

from games.views import game_detail
from .views import index


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', game_detail, name='detail'),
]
