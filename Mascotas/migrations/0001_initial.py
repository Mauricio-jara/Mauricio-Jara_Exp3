# Generated by Django 4.2.1 on 2023-06-20 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('dv', models.IntegerField(max_length=5, primary_key=True, serialize=False, verbose_name='Dv')),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=100, verbose_name='Descripcion')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen')),
            ],
        ),
    ]