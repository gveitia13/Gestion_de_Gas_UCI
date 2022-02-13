from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    solapin = models.CharField(max_length=10, verbose_name='Solapin', blank=True, null=True)
    role = models.CharField(max_length=50, choices=(
        ('client', 'Cliente'),
        ('admin', 'Administrador'),
        ('distributor', 'Distribuidor'),
    ), verbose_name='Rol')

    def __str__(self):
        return self.first_name if self.first_name else self.username

    def save(self, *args, **kwargs):
        # cosas y cosas jeje
        super(User, self).save()
