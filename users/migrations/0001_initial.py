# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=139)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, blank=True, help_text='Posted on: ', null=True)),
                ('user', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Ripple',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ripple_text', models.CharField(blank=True, max_length=139)),
                ('ripple_date', models.DateTimeField(default=django.utils.timezone.now, blank=True, help_text='Posted on: ', null=True)),
                ('original_post', models.ForeignKey(to='users.Post')),
            ],
            options={
                'ordering': ['-ripple_date'],
            },
        ),
    ]
