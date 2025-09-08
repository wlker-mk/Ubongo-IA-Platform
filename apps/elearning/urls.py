#from django.urls import path, include

#urlpatterns = [
    # path("courses/", include("apps.elearning.courses.urls")),
    # path("lessons/", include("apps.elearning.lessons.urls")),
    # path("quiz/", include("apps.elearning.quiz.urls")),
    #path("progress/", include("apps.elearning.progress_tracking.urls")),
    #path("certification/", include("apps.elearning.certification.urls")),
    #path("forum/", include("apps.elearning.forum.urls")),
#]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]


