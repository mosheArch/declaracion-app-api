from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'), )

    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    genero = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=True)
    is_staff = models.BooleanField(default=False)
    # last_login = models.DateTimeField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()


def get_short_name(self):
    return self.username


def get_full_name(self):
    return self.nombres + ' '+self.apellidos
