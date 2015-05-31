# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopay', '0002_auto_20150530_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='ip_address',
            field=models.GenericIPAddressField(default=''),
            preserve_default=False,
        ),
    ]
