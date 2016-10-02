# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_ripple'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ripple',
            options={'ordering': ['original_post']},
        ),
        migrations.RenameField(
            model_name='ripple',
            old_name='original_post_owner',
            new_name='original_post',
        ),
    ]
