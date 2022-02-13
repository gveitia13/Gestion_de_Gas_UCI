from django.core.validators import MaxValueValidator, RegexValidator, MinValueValidator
from django.db import models

from Reserva_de_gas import settings


# Create your models here.

class Contrato(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name='Nombre del cliente')
    age = models.PositiveSmallIntegerField(verbose_name='Edad',
                                           validators=[MaxValueValidator(100, message='Entre una edad entre 23 y 100'),
                                                       MinValueValidator(23, message='Entre una edad entre 23 y 100')])
    ci = models.CharField(verbose_name='Carnet de identidad',
                          validators=[
                              RegexValidator(r'^\d{1,10}$',
                                             message='Entre un carnet de identidad válido(11 dígitos)'), ],
                          max_length=11, min_length=11)
    validity = models.PositiveSmallIntegerField(verbose_name='Tiempo de vigencia (meses)', validators=[
        MaxValueValidator(24, message='El tiempo debe ser menor a 25 meses')])
    date_creation = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creado')

    def __str__(self):
        return f'Contrato {self.id} de: {str(self.user)}'

    class Meta:
        ordering = ['date_creation', 'validity']
