# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(unique=True)),
                ('authors', models.TextField()),
                ('abstract', models.TextField()),
                ('documentURL', models.URLField()),
                ('documentFree', models.BooleanField()),
                ('pubmedID', models.CharField(max_length=128)),
                ('citation', models.CharField(max_length=128)),
                ('abstractPool', models.BooleanField(default=True)),
                ('documentPool', models.BooleanField(default=False)),
                ('finalPool', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='query',
            name='review',
            field=models.ForeignKey(to='mainapp.Review'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='review',
            field=models.ForeignKey(to='mainapp.Review'),
            preserve_default=True,
        ),
    ]
