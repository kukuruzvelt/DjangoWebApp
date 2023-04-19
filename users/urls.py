from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register_page),
    path('', include('django.contrib.auth.urls')),
    #path('login', views.login_page),
]