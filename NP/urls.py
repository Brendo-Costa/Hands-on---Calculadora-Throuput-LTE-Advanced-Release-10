from django.urls import path
from . import views

urlpatterns = [
    path('', views.np, name='np'), # Caminho para a view.np
]