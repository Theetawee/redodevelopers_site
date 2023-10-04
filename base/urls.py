from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from main.sitemap import StaticViewSitemap

sitemaps={
    'sites':StaticViewSitemap
}




urlpatterns = [
    path("admin/tawee", admin.site.urls),
    path("", include("main.urls")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'main.views.custom_404_view'
handler400 = 'main.views.custom_404_view'
handler500 = 'main.views.custom_500_view'
handler403 = 'main.views.custom_404_view'

