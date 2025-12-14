"""
URL configuration for patient_system project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Custom Admin (Not Django's built-in admin)
    path('management/', include('records.admin_urls')),
    
    # Django admin for OAuth configuration only
    path('django-admin/', admin.site.urls),
    
    # Social Authentication (Allauth)
    path('accounts/', include('allauth.urls')),
    
    # Main application URLs
    path('', include('records.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
