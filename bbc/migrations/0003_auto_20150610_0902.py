# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbc', '0002_study_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biobank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
        ),
        migrations.AlterField(
            model_name='study',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
