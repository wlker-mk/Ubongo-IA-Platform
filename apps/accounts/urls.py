from django.urls import path, include
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", lambda request: redirect("login")),  # redirige /accounts/ vers /accounts/login/
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
]

