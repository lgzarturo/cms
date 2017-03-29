from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

admin.site.site_header = 'Panel de Control : Famisoft'

admin.site.site_title = 'Famisoft Software y Desarrollo a la Medida'

urlpatterns = [
    url(r'^', include('web.urls', namespace="web")),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
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
