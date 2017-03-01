from django.contrib import admin

from products.models import Product


@admin.register(Product)
class JoinAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

