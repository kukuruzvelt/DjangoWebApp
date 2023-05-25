from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('register', views.register_page),
    re_path(r'^profile/(?P<message>\w{0,20})$', views.profile_page),
    path('pay', views.pay_page),
    path('', include('django.contrib.auth.urls')),
]