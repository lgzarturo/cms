from django.shortcuts import render

from products.models import ProductFeatured


def home(request):
    featured_img = ProductFeatured.objects.filter(active=True).order_by("?").first()
    context = {
        "title": "Pagina web principal",
        "featured_img": featured_img
    }
    return render(request, "web/home.html", context)
