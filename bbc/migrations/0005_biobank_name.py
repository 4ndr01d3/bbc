# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbc', '0004_study_biobank'),
    ]

    operations = [
        migrations.AddField(
            model_name='biobank',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
