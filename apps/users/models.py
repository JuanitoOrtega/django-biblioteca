from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    username = models.CharField(max_length=20, unique=True, verbose_name='Nombre de usuario')
    email = models.EmailField(max_length=50, verbose_name='Correo electrónico')
    first_name = models.CharField(max_length=50, blank=True, verbose_name='Nombres')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Apellidos')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, verbose_name='Género')
    is_staff = models.BooleanField(default=False, verbose_name='Es miembro del staff')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.username