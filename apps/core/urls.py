
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("diagnostic/", views.diagnostic, name="diagnostic"),
    path("expertIA/", views.expertIA, name="expertIA"),
    path("about/", views.about, name="about"),
    path("community/", views.community, name="community"),
]
