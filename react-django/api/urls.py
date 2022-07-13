from django.urls import path
from django.views.generic import TemplateView
from api.views import TestApiView

urlpatterns = [
    # template
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('test/', TestApiView.as_view(), name='test'),
]
