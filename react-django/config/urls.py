from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
