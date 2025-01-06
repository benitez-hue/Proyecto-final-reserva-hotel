# Generated by Django 5.1.4 on 2024-12-16 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=100)),
                ('posicion', models.CharField(max_length=50)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
