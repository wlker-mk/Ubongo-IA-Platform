from django.urls import path
from . import views

urlpatterns = [
    path("diagnostic/", views.index, name="diagnostic"),
]

