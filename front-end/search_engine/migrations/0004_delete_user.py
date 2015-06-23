# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0003_auto_20150607_1428'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
