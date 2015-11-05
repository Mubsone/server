# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151105_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mubsoneuser',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
