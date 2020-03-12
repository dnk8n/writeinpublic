# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuntium', '0007_switch_fks_to_popoloperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='ratelimiter',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
