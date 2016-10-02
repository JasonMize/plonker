# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160930_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ripple',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('original_post_owner', models.ForeignKey(to='users.Post', null=True, blank=True)),
            ],
            options={
                'ordering': ['original_post_owner'],
            },
        ),
    ]
