# Generated by Django 5.1.1 on 2024-11-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_alter_servicio_descripcion_alter_servicio_duracion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='img',
            field=models.CharField(default='#', max_length=100, verbose_name='UrlImage'),
        ),
    ]
