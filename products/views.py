from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from products.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "product/list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/detail.html"


