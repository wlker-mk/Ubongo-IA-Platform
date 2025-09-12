from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from .models import User  # ton User custom

class LoginV(View):
    def get(self, request):
        return render(request, "auth/login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_type = request.POST.get("user_type")

        # Vérification email
        try:
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            messages.error(request, "Cet email n'existe pas.")
            return render(request, "auth/login.html")

        # Authentification
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            # Redirection selon type
            if user_type == "expert":
                return redirect("/dashboard/expert/")
            elif user_type == "entreprise":
                return redirect("/dashboard/entreprise/")
            return redirect("/")  # apprenant par défaut
        else:
            messages.error(request, "Mot de passe incorrect.")
            return render(request, "auth/login.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class Register(View):
    def get(self, request):
        return render(request, "auth/register.html")

    def post(self, request):
        form_type = request.POST.get("form_type")

        try:
            email = request.POST.get("email")
            password = request.POST.get("password")

            if User.objects.filter(email=email).exists():
                messages.error(request, "Cet email est déjà utilisé.")
                return render(request, "auth/register.html")

            if form_type == "entreprise":
                user = User.objects.create_user(
                    username=request.POST.get("company_name"),
                    email=email,
                    password=password,
                    user_type='entreprise',
                    sector=request.POST.get("sector"),
                    company_size=request.POST.get("size"),
                    first_name="Entreprise",
                    last_name=request.POST.get("sector")
                )
                messages.success(request, "Compte entreprise créé avec succès !")
                return redirect("login")

            elif form_type == "expert":
                user = User.objects.create_user(
                    username=request.POST.get("full_name"),
                    email=email,
                    password=password,
                    user_type='expert',
                    speciality=request.POST.get("speciality"),
                    experience=request.POST.get("experience"),
                    first_name="Expert",
                    last_name=request.POST.get("speciality")
                )
                messages.success(request, "Compte expert créé avec succès !")
                return redirect("login")

        except Exception as e:
            messages.error(request, f"Erreur lors de l'inscription : {e}")
            return render(request, "auth/register.html")

