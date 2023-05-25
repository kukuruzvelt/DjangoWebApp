from django.urls import path

from . import views

urlpatterns = [
    path('catalog', views.catalog),
    path('cart', views.cart),
    path('buy', views.buy),
    path('orders', views.orders),
]
