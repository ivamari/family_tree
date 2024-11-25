from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('api.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
]
