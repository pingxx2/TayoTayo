from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from tayo import views

urlpatterns = [
    path('', views.main, name='main'),
    path("admin/", admin.site.urls),
    path("iot/", include('iot.urls')),
    path("tayo/", include('tayo.urls')),
    path('common/', include('common.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

