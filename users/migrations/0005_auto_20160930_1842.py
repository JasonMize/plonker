# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.localtime, null=True, help_text='Posted on:'),
        ),
    ]
