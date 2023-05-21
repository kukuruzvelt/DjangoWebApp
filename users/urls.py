from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register_page),
    path('profile', views.profile_page),
    path('pay', views.pay_page),
    path('', include('django.contrib.auth.urls')),
]