from django.conf.urls import url

from products.views import VariationListView
from .views import ProductDetailView, ProductListView


urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='inventory'),
]
