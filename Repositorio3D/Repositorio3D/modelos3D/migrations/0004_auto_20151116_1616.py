# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('modelos3D', '0003_auto_20151116_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenesmodelos',
            name='imagen',
            field=models.ImageField(default=b'/home/aluque/PFC/Repositorio3D/Repositorio3D/Repositorio3D/media/image_not_available/image-not-available.png', storage=django.core.files.storage.FileSystemStorage(location=b'Repositorio3D/media/imagenes'), upload_to=b'', blank=True),
        ),
    ]
