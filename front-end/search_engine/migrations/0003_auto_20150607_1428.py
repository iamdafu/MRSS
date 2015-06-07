# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0002_auto_20150607_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourceurl',
            name='pub_date',
            field=models.DateField(verbose_name=b'search date'),
        ),
    ]
