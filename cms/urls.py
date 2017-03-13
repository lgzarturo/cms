from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^', include('web.urls', namespace="web")),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include("articles.urls", namespace="article")),
    url(r'^products/', include("products.urls", namespace="product")),
    url(r'^categories/', include("products.urls_categories", namespace="category")),
    url(r'^newsletter/', include("newsletters.urls", namespace="newsletter")),
    url(r'^games/', include("games.urls", namespace="game")),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
