from django.contrib import admin

from products.models import Product, Variation, ProductImage, Category, ProductFeatured


class ProductImageInline(admin.TabularInline):
    fields = ['image', ]
    model = ProductImage
    extra = 0


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'price', ]
    inlines = [ProductImageInline, VariationInline, ]

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
    fields = ['product', 'image', 'title', 'text', 'text_css_color', 'make_image_background', 'show_price', 'active', ]

    class Meta:
        model = ProductFeatured
