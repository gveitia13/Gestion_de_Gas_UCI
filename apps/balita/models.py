from crum import get_current_user
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
                              RegexValidator(r'^\d{1,11}$',
                                             message='Entre un carnet de identidad válido(11 dígitos)'), ],
                          max_length=11, )
    validity = models.PositiveSmallIntegerField(verbose_name='Tiempo de vigencia (meses)', validators=[
        MaxValueValidator(24, message='El tiempo debe ser menor a 25 meses')])
    date_creation = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creado')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        self.user = user
        super(Contrato, self).save()

    def __str__(self):
        return f'Contrato {self.id} de: {str(self.user)}'

    class Meta:
        ordering = ['date_creation', 'validity']


class Balita(models.Model):
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Precio', default=180.0)
    quantity = models.PositiveIntegerField(verbose_name='Cantidad', blank=True, null=True, default=1)


# class Incidente(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
#     description = models.TextField(max_length=500, verbose_name='Description del problema')
#
#     def save(self, force_insert=False, force_update=False, using=None,
#              update_fields=None):
#         user = get_current_user()
#         self.user = user
#         super(Incidente, self).save()
#
#     def __str__(self):
#         return f'Incidente de: {str(self.user)}'


class Informe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario', on_delete=models.CASCADE,
                             null=True, blank=True, )
    date_creation = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creado')
    balita = models.ForeignKey(Balita, verbose_name='Producto (Balita de Gas)', on_delete=models.CASCADE, null=True,
                               blank=True)

    class Meta:
        abstract = True


class InformeIncidencia(Informe):
    # Lo hace el cliente asere
    motive = models.TextField(max_length=250, verbose_name='Motivo del reporte')

    def __str__(self):
        return f'{str(self.user)}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        self.user = user
        try:
            self.balita = Balita.objects.first()
        except:
            pass
        super(InformeIncidencia, self).save()

    class Meta:
        ordering = ['date_creation']


class InformeReserva(Informe):
    # Lo hace el cliente asere
    quantity = models.PositiveSmallIntegerField(verbose_name='Cantidad de balitas')

    def __str__(self):
        return f'{str(self.user)}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        self.user = user
        try:
            self.balita = Balita.objects.first()
        except:
            pass
        super(InformeReserva, self).save()

    class Meta:
        ordering = ['date_creation']


class InformeVenta(Informe):
    # Lo hace el distribuidor
    receiver = models.CharField(max_length=100, verbose_name='Nombre del recibidor')
    quantity = models.PositiveSmallIntegerField(verbose_name='Cantidad de balitas')
    importe = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Importe total', default=0)

    def __str__(self):
        return f'{str(self.user)}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        self.user = user
        try:
            self.balita = Balita.objects.first()
        except:
            pass
        super(InformeVenta, self).save()

    class Meta:
        ordering = ['date_creation']
