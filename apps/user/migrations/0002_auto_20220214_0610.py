# Generated by Django 3.2.12 on 2022-02-14 11:10

import apps.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('client', 'Cliente'), ('admin', 'Administrador'), ('distributor', 'Distribuidor')], max_length=50, null=True, verbose_name='Rol'),
        ),
        migrations.AlterField(
            model_name='user',
            name='solapin',
            field=models.CharField(default=123, max_length=7, unique=True, validators=[apps.user.models.ValidateSolapin], verbose_name='Solapín'),
            preserve_default=False,
        ),
    ]
