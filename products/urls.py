from django.urls import path, include
from . import views

urlpatterns = [
    path('catalog', views.catalog),
    path('cart', views.cart),
]