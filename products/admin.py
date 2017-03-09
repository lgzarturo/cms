from django.contrib import admin

from products.models import Product, Variation, ProductImage, Category, ProductFeatured


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    class Meta:
        model = Variation


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


@admin.register(ProductFeatured)
class ProductFeaturedAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductFeatured
