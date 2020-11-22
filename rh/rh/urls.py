
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path("accounts/", include("allauth.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls'))
]
