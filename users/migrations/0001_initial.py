# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True, help_text='Posted on:')),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
    ]
