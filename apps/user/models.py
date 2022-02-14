from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


def ValidateSolapin(value):
    if len(str(value)) < 7:
        raise ValidationError(
            'El solapín debe ser de 7 caracteres',
            params={'value': value}
        )


class User(AbstractUser):
    solapin = models.CharField(max_length=7, verbose_name='Solapín',
                               validators=[ValidateSolapin], unique=True)
    role = models.CharField(max_length=50, choices=(
        ('client', 'Cliente'),
        ('admin', 'Administrador'),
        ('distributor', 'Distribuidor'),
    ), verbose_name='Rol')

    def __str__(self):
        return self.get_full_name() if self.first_name else self.username

    def save(self, *args, **kwargs):
        passw = self.password
        if self.pk is None:
            self.set_password(passw)
        else:
            user = User.objects.get(pk=self.pk)
            if user.password != passw:
                self.set_password(passw)
        # self.set_password(self.password)
        # transaction.on_commit(lambda: self.groups.add(Group.objects.first()))
        super(User, self).save()
