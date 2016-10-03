# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20161003_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ripple',
            name='original_post_owner',
        ),
    ]
