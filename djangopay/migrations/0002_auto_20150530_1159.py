# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='product',
        ),
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
