from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.shortcuts import redirect
from . import views
from .views import  Register, LoginV

urlpatterns = [
    path("", lambda request: redirect("login")),  # redirige /accounts/ vers /accounts/login/
    path("login/", LoginV.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

