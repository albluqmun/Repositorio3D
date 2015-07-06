# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesModelos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Model3D',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('valoracion', models.DecimalField(default=0, max_digits=4, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='TagsModelos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=50)),
                ('modelo', models.ForeignKey(to='modelos3D.Model3D')),
            ],
        ),
        migrations.AddField(
            model_name='imagenesmodelos',
            name='modelo',
            field=models.ForeignKey(to='modelos3D.Model3D'),
        ),
    ]
