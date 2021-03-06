# Generated by Django 3.2.12 on 2022-02-14 09:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('balita', '0003_auto_20220213_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='informereserva',
            name='date_to_reserve',
            field=models.DateField(blank=True, null=True, verbose_name='Reservar para:'),
        ),
        migrations.AlterField(
            model_name='informeincidencia',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='informereserva',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='informeventa',
            name='importe',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, validators=[django.core.validators.MinValueValidator(0, message='El importe debe ser positivo xd')], verbose_name='Importe total'),
        ),
        migrations.AlterField(
            model_name='informeventa',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.DeleteModel(
            name='Incidente',
        ),
    ]
