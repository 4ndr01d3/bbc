# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbc', '0003_auto_20150610_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='biobank',
            field=models.ForeignKey(default=None, to='bbc.Biobank'),
        ),
    ]
