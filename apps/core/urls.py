
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("diagnostic/", views.diagnostic, name="diagnostic"),
    path("about/", views.about, name="about"),
]
