from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    user_type = models.CharField(
        max_length=20,
        choices=[('expert', 'Expert'), ('entreprise', 'Entreprise')]
    )

    # ✅ Ajoutez ces nouveaux champs
    sector = models.CharField(max_length=100, blank=True, null=True)
    company_size = models.IntegerField(blank=True, null=True)
    speciality = models.CharField(max_length=100, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)

    # Remplacez le gestionnaire par défaut
    objects = CustomUserManager()

    # Utilisez email comme identifiant au lieu de username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email