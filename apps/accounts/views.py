from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from .models import User


class LoginV(View):
    def get(self, request):
        return render(request, "auth/login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Authentification avec email
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            redirect_map = {
                "expert": "/dashboard/expert.html",
                "entreprise": "/dashboard/entreprise.html",
            }
            return redirect(redirect_map.get(user.user_type, "/"))  # redirection par défaut
        else:
            messages.error(request, "Email ou mot de passe incorrect.")
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
                company_name = request.POST.get("company_name")
                if User.objects.filter(username=company_name).exists():
                    messages.error(request, "Ce nom d'entreprise est déjà utilisé.")
                    return render(request, "auth/register.html")

                user = User.objects.create_user(
                    username=company_name,
                    email=email,
                    password=password,
                    user_type='entreprise',
                    sector=request.POST.get("sector"),
                    company_size=request.POST.get("size"),
                    first_name=company_name,  # Utilise un champ plus approprié
                    last_name=request.POST.get("sector")
                )
                messages.success(request, "Compte entreprise créé avec succès !")
                return redirect("login")

            elif form_type == "expert":
                full_name = request.POST.get("full_name")
                if User.objects.filter(username=full_name).exists():
                    messages.error(request, "Ce nom d'expert est déjà utilisé.")
                    return render(request, "auth/register.html")

                # Séparer le nom complet en prénom et nom si possible
                name_parts = full_name.split(' ', 1)
                first_name = name_parts[0]
                last_name = name_parts[1] if len(name_parts) > 1 else ""

                user = User.objects.create_user(
                    username=full_name,
                    email=email,
                    password=password,
                    user_type='expert',
                    speciality=request.POST.get("speciality"),
                    experience=request.POST.get("experience"),
                    first_name=first_name,
                    last_name=last_name
                )
                messages.success(request, "Compte expert créé avec succès !")
                return redirect("login")

        except Exception as e:
            messages.error(request, f"Erreur lors de l'inscription : {str(e)}")
            return render(request, "auth/register.html")