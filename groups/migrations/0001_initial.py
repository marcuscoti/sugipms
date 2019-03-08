# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-30 18:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('CH', 'CABLING HORIZONTAL'), ('CV', 'CABLING VERTICAL'), ('HW', 'INSTALA\xc7\xc3O E CONFIGURA\xc7\xc3O DE HW'), ('INFRA', 'INFRA B\xc1SICA'), ('PLAN', 'PLANEJAMENTO'), ('SUGI', 'SUGI+ SERVIDORES')], default='CH', max_length=8)),
                ('description', models.TextField(blank=True, max_length=60, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='GroupStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(default=datetime.datetime(2019, 1, 30, 18, 33, 20, 739000, tzinfo=utc))),
                ('end', models.DateField(default=datetime.datetime(2019, 1, 30, 18, 33, 20, 739000, tzinfo=utc))),
                ('duration', models.IntegerField(default=0)),
                ('act_ended', models.IntegerField(default=0)),
                ('act_program', models.IntegerField(default=0)),
                ('act_late', models.IntegerField(default=0)),
                ('act_total', models.IntegerField(default=0)),
                ('deliveried', models.DecimalField(decimal_places=2, default=0, max_digits=2)),
                ('target', models.DecimalField(decimal_places=2, default=0, max_digits=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
            ],
            options={
                'verbose_name_plural': 'GroupStatus',
            },
        ),
    ]
