import os

# === Définition des apps principales et modulaires ===
apps = {
    "users": {},
    "auth": {},
    "consultations": {},
    "bookings": {},
    "payments": {"gateways": ["stripe_service.py", "paypal_service.py", "mobilemoney_service.py", "crypto_service.py"]},
    "notifications": {"services": ["email_service.py", "sms_service.py", "push_service.py", "inapp_service.py"]},
    "webinars": {"integrations": ["zoom_service.py", "teams_service.py", "jitsi_service.py", "google_meet_service.py"]},
    "gamification": {"services": ["badge_service.py", "loyalty_service.py", "referral_service.py", "discount_service.py"]},
    "cms": {"articles": [], "comments": [], "ratings": [], "suggestions": []},
    "projects": {},
    "integrations": {
        "calendars": ["google_calendar.py", "outlook_calendar.py", "apple_calendar.py"],
        "storage": ["dropbox_service.py", "gdrive_service.py", "s3_service.py"],
        "crm": ["salesforce_service.py", "hubspot_service.py"],
    },
    "communication": {"chat": [], "files": [], "code_snippets": [], "feedback": []},
    "analytics": {},
    "security": {},
    "etl": {"extractor": ["extract.py"], "transformer": ["transform.py"], "loader": ["load.py"], "scheduler": ["schedule.py"]},
    "elearning": {
        "courses": ["models.py", "views.py", "urls.py", "serializers.py"],
        "lessons": ["models.py", "views.py", "urls.py", "serializers.py"],
        "quiz": ["models.py", "views.py", "urls.py", "serializers.py"],
        "progress_tracking": ["models.py", "views.py", "urls.py"],
        "certification": ["models.py", "views.py", "urls.py"],
        "forum": ["models.py", "views.py", "urls.py", "serializers.py"],
        "resources": ["models.py", "views.py", "urls.py"],
        "services": ["quiz_service.py", "enrollment_service.py"],
    },
    "ai": {},
    "api": {},
    "core": {},
}

base_path = os.path.join("apps")

# === Contenu minimal par défaut ===
content_defaults = {
    "models.py": '''from django.db import models

class Example(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
''',

    "views.py": '''from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Hello from module!"})
''',

    "urls.py": '''from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
''',

    "serializers.py": '''from rest_framework import serializers
from .models import Example

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = "__all__"
''',

    "quiz_service.py": '''class QuizService:
    def grade(self, answers):
        # TODO: implémenter correction quiz
        return {"score": len(answers), "passed": True}
''',

    "enrollment_service.py": '''class EnrollmentService:
    def enroll(self, user, course):
        # TODO: implémenter logique d'inscription
        return {"user": user, "course": course, "status": "enrolled"}
'''
}

# === Génération des apps ===
all_apps = []
for app, modules in apps.items():
    app_path = os.path.join(base_path, app)
    os.makedirs(app_path, exist_ok=True)
    open(os.path.join(app_path, "__init__.py"), "w").close()

    # fichiers racine pour chaque app
    for file in ["models.py", "views.py", "urls.py", "serializers.py"]:
        file_path = os.path.join(app_path, file)
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content_defaults.get(file, ""))

    # création des sous-modules
    for module, files in modules.items():
        module_path = os.path.join(app_path, module)
        os.makedirs(module_path, exist_ok=True)
        open(os.path.join(module_path, "__init__.py"), "w").close()
        for file in files:
            file_path = os.path.join(module_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content_defaults.get(file, ""))

    all_apps.append(f"apps.{app}")

print("✅ Structure des apps générée avec succès !")

# === Mise à jour de INSTALLED_APPS dans settings.py ===
settings_path = os.path.join("config", "settings.py")

if os.path.exists(settings_path):
    with open(settings_path, "r", encoding="utf-8") as f:
        settings_content = f.read()

    new_apps = [a for a in all_apps if a not in settings_content]

    if new_apps:
        updated_content = settings_content.replace(
            "INSTALLED_APPS = [",
            "INSTALLED_APPS = [\n    " + ",\n    ".join([f"'{a}'" for a in new_apps]) + ","
        )

        with open(settings_path, "w", encoding="utf-8") as f:
            f.write(updated_content)

        print(f"✅ {len(new_apps)} apps ajoutées à INSTALLED_APPS")
    else:
        print("ℹ️ Toutes les apps sont déjà dans INSTALLED_APPS")
else:
    print("⚠️ settings.py introuvable, ajout impossible")

# === Mise à jour de config/urls.py ===
urls_path = os.path.join("config", "urls.py")

if os.path.exists(urls_path):
    with open(urls_path, "r", encoding="utf-8") as f:
        urls_content = f.read()

    new_routes = []
    for app in apps.keys():
        route_line = f'    path("{app}/", include("apps.{app}.urls")),'
        if route_line not in urls_content:
            new_routes.append(route_line)

    if new_routes:
        if "urlpatterns = [" in urls_content:
            updated_urls = urls_content.replace(
                "urlpatterns = [",
                "urlpatterns = [\n" + "\n".join(new_routes) + "\n"
            )
            if "from django.urls import path, include" not in updated_urls:
                updated_urls = "from django.urls import path, include\n\n" + updated_urls

            with open(urls_path, "w", encoding="utf-8") as f:
                f.write(updated_urls)

            print(f"✅ {len(new_routes)} nouvelles routes ajoutées à urls.py")
    else:
        print("ℹ️ Toutes les routes existent déjà")
else:
    print("⚠️ urls.py introuvable, ajout impossible")
