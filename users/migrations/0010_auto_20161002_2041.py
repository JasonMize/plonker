# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_ripple_original_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(blank=True, max_length=139),
        ),
        migrations.AlterField(
            model_name='ripple',
            name='original_post',
            field=models.OneToOneField(to='users.Post', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ripple',
            name='original_post_owner',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
    ]
