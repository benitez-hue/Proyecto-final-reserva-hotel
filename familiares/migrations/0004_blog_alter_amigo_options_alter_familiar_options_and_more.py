# Generated by Django 5.1.4 on 2024-12-31 16:30

import django.core.validators
import django.db.models.deletion
import familiares.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0003_amigo_familiar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Ingrese el título del blog.', max_length=200, verbose_name='Título')),
                ('subtitulo', models.CharField(blank=True, help_text='Ingrese un subtítulo para el blog (opcional).', max_length=200, null=True, verbose_name='Subtítulo')),
                ('cuerpo', models.TextField(help_text='Ingrese el contenido del blog.', verbose_name='Contenido')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicación')),
                ('imagen', models.ImageField(blank=True, help_text='Suba una imagen relacionada con el blog (opcional).', null=True, upload_to=familiares.models.Blog.upload_to, verbose_name='Imagen asociada')),
            ],
            options={
                'verbose_name_plural': 'Blogs',
                'ordering': ['-fecha'],
            },
        ),
        migrations.AlterModelOptions(
            name='amigo',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Amigos'},
        ),
        migrations.AlterModelOptions(
            name='familiar',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Familiares'},
        ),
        migrations.AlterModelOptions(
            name='trabajo',
            options={'ordering': ['nombre_empresa'], 'verbose_name_plural': 'Trabajos'},
        ),
        migrations.AlterField(
            model_name='amigo',
            name='email',
            field=models.EmailField(help_text='Ingrese una dirección de correo electrónico válida.', max_length=254, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='amigo',
            name='familiar',
            field=models.ForeignKey(blank=True, help_text='Seleccione un familiar relacionado, si aplica.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='amigos', to='familiares.familiar', verbose_name='Familiar relacionado'),
        ),
        migrations.AlterField(
            model_name='amigo',
            name='nombre',
            field=models.CharField(help_text='Ingrese el nombre completo del amigo.', max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='amigo',
            name='telefono',
            field=models.CharField(help_text='Ingrese el número de teléfono del amigo (incluyendo código de país si es necesario).', max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', 'El número de teléfono debe tener entre 9 y 15 dígitos.')], verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='edad',
            field=models.IntegerField(help_text='Ingrese la edad del familiar (de 0 a 120 años).', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)], verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.DateField(help_text='Ingrese la fecha de nacimiento del familiar.', verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='nombre',
            field=models.CharField(help_text='Ingrese el nombre completo del familiar.', max_length=100, verbose_name='Nombre completo'),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='nombre_empresa',
            field=models.CharField(help_text='Ingrese el nombre de la empresa.', max_length=100, verbose_name='Nombre de la empresa'),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='posicion',
            field=models.CharField(help_text='Ingrese el cargo o posición desempeñada.', max_length=50, verbose_name='Posición o cargo'),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='salario',
            field=models.DecimalField(decimal_places=2, help_text='Ingrese el salario asociado al trabajo.', max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Salario'),
        ),
        migrations.AddConstraint(
            model_name='trabajo',
            constraint=models.UniqueConstraint(fields=('nombre_empresa', 'posicion'), name='unique_empresa_posicion'),
        ),
        migrations.AddField(
            model_name='blog',
            name='autor',
            field=models.ForeignKey(help_text='Seleccione el autor del blog.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]