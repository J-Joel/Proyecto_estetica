# Generated by Django 5.1.2 on 2024-11-07 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=50, verbose_name='Apellido')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='Email')),
                ('telefono', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.telefono')),
            ],
        ),
    ]
