from django.urls import path, include

"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("users/", include("apps.users.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("consultations/", include("apps.consultations.urls")),
    path("bookings/", include("apps.bookings.urls")),
    path("payments/", include("apps.payments.urls")),
    path("notifications/", include("apps.notifications.urls")),
    path("webinars/", include("apps.webinars.urls")),
    path("gamification/", include("apps.gamification.urls")),
    path("cms/", include("apps.cms.urls")),
    path("projects/", include("apps.projects.urls")),
    path("integrations/", include("apps.integrations.urls")),
    path("communication/", include("apps.communication.urls")),
    path("analytics/", include("apps.analytics.urls")),
    path("security/", include("apps.security.urls")),
    path("etl/", include("apps.etl.urls")),
    path("elearning/", include("apps.elearning.urls")),
    path("ai/", include("apps.ai.urls")),
    path("api/", include("apps.api.urls")),
    path("core/", include("apps.core.urls")),

    path('admin/', admin.site.urls),
]
