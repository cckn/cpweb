from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('areas/<str:area>/', views.areas)
]
