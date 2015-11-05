# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mubsoneuser',
            name='contests',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mubsoneuser',
            name='videos',
            field=models.IntegerField(default=0),
        ),
    ]
