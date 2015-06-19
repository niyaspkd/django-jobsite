# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=255, verbose_name=b'User Name')),
                ('first_name', models.CharField(max_length=128, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=128, verbose_name=b'Last Name')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('role', models.CharField(max_length=1, choices=[(b'1', b'Employer'), (b'2', b'Employee')])),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='apply',
            name='job_id',
            field=models.ForeignKey(to='jobsite.Jobs'),
            preserve_default=True,
        ),
    ]
