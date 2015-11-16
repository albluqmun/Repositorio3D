# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('modelos3D', '0002_auto_20151017_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenesmodelos',
            name='imagen',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'Repositorio3D/media/imagenes'), upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='tagsmodelos',
            name='tag',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
