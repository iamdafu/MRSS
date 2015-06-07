# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recommendation_text', models.CharField(max_length=200)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SearchWord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('search_word_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SourceUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_url', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('recommendation', models.ForeignKey(to='search_engine.Recommendation')),
            ],
        ),
        migrations.AddField(
            model_name='recommendation',
            name='search_word',
            field=models.ForeignKey(to='search_engine.SearchWord'),
        ),
    ]
