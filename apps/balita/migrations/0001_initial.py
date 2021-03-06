# Generated by Django 3.2.12 on 2022-02-13 06:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Balita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=180.0, max_digits=9, verbose_name='Precio')),
                ('quantity', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Cantidad')),
            ],
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=100, verbose_name='Nombre del recibidor')),
                ('date_creation', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creado')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Cantidad de balitas')),
                ('type', models.CharField(choices=[('entrega', 'Entrega'), ('venta', 'Venta'), ('reservacion', 'Reservación')], max_length=100, verbose_name='Tipo de informe')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Descripción del informe')),
                ('balita', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='balita.balita', verbose_name='Producto (Balita de Gas)')),
                ('deliver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Entregador')),
            ],
            options={
                'ordering': ['date_creation'],
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del cliente')),
                ('age', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100, message='Entre una edad entre 23 y 100'), django.core.validators.MinValueValidator(23, message='Entre una edad entre 23 y 100')], verbose_name='Edad')),
                ('ci', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^\\d{1,10}$', message='Entre un carnet de identidad válido(11 dígitos)')], verbose_name='Carnet de identidad')),
                ('validity', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(24, message='El tiempo debe ser menor a 25 meses')], verbose_name='Tiempo de vigencia (meses)')),
                ('date_creation', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creado')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_creation', 'validity'],
            },
        ),
    ]
