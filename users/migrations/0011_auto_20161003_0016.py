# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20161002_2041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ripple',
            options={'ordering': ['-ripple_date']},
        ),
        migrations.AddField(
            model_name='ripple',
            name='ripple_date',
            field=models.DateTimeField(help_text='Posted on: ', blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='ripple',
            name='ripple_text',
            field=models.CharField(max_length=139, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(help_text='Posted on: ', blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
