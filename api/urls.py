from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_view, name='vue-api'),
]
