
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("diagnostic/", views.diagnostic, name="diagnostic"),
    path("expert/", views.expert, name="expertIA"),
    path("fiche_expert/", views.fiche_expert, name="fiche_expert"),
    path("about/", views.about, name="about"),
    path("community/", views.community, name="community"),
]
