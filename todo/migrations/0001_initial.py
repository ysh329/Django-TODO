# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('priority', models.IntegerField(default=2, choices=[(1, b'Low'), (2, b'Normal'), (3, b'High')])),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-priority', 'title'],
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=250)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='todo_list',
            field=models.ForeignKey(to='todo.List'),
        ),
    ]
