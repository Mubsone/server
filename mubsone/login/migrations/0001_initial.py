# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('rating', models.IntegerField(default=0)),
                ('fans', models.IntegerField(default=0)),
                ('biography', models.CharField(max_length=200)),
                ('is_banned', models.BooleanField(default=False)),
                ('email', models.CharField(max_length=45)),
                ('avatar', models.CharField(max_length=45)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_premium', models.BooleanField(default=False)),
            ],
        ),
    ]
