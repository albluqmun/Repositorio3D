# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modelos3D', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagenesmodelos',
            options={'verbose_name': 'Imagen', 'verbose_name_plural': 'Im\xe1genes'},
        ),
        migrations.AlterModelOptions(
            name='model3d',
            options={'verbose_name': 'Modelo 3D', 'verbose_name_plural': 'Modelos 3D'},
        ),
        migrations.AlterModelOptions(
            name='tagsmodelos',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AddField(
            model_name='model3d',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='imagenesmodelos',
            name='imagen',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'Repositorio3D/media/imagenes'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='model3d',
            name='valoracion',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
