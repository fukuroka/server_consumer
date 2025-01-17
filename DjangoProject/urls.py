import os

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TestRC.urls')),
    path('', include('SecondTestRC.urls')),

    path('', RedirectView.as_view(url='/backend/')),
    path('backend/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('backend/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static('node_modules', document_root=os.path.join(settings.BASE_DIR, 'node_modules'))
    urlpatterns += static('media', document_root=settings.MEDIA_ROOT)
