# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malfunction_start_time', models.DateField()),
                ('malfunction_stop_time', models.DateField()),
                ('malfunction_type', models.IntegerField()),
                ('notify_persion', models.CharField(max_length=50)),
                ('record_persion', models.CharField(db_index=True, max_length=50)),
                ('malfunction_content', models.TextField()),
                ('event_status', models.BooleanField(db_index=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RecordCloseNotify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_ip', models.GenericIPAddressField()),
                ('service', models.TextField()),
                ('malfunction_start_time', models.DateField()),
                ('malfunction_stop_time', models.DateField()),
                ('notify_persion', models.CharField(max_length=50)),
                ('record_persion', models.CharField(db_index=True, max_length=50)),
                ('malfunction_content', models.TextField()),
                ('event_status', models.BooleanField(db_index=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RecordMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_ip', models.GenericIPAddressField()),
                ('malfunction_time', models.DateField()),
                ('notify_persion', models.CharField(max_length=50)),
                ('record_persion', models.CharField(db_index=True, max_length=50)),
                ('malfunction_content', models.TextField()),
                ('event_status', models.BooleanField(db_index=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RecordMachineRepiar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_ip', models.GenericIPAddressField()),
                ('malfunction_time', models.DateField()),
                ('notify_persion', models.CharField(max_length=50)),
                ('record_persion', models.CharField(db_index=True, max_length=50)),
                ('malfunction_content', models.TextField()),
                ('event_status', models.BooleanField(db_index=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RecordMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malfunction_start_time', models.DateField()),
                ('malfunction_stop_time', models.DateField()),
                ('notify_persion', models.CharField(max_length=50)),
                ('record_persion', models.CharField(db_index=True, max_length=50)),
                ('malfunction_content', models.TextField()),
                ('event_status', models.BooleanField(db_index=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RecordNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malfunction_start_time', models.DateField()),
                ('malfunction_stop_time', models.DateField()),
                ('malfunction_type', models.IntegerField()),
                ('malfunction_responsibility', models.IntegerField()),
                ('notify_persion', models.CharField(max_length=50)),
                ('record_persion', models.CharField(db_index=True, max_length=50)),
                ('malfunction_content', models.TextField()),
                ('event_status', models.BooleanField(db_index=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RecordOther',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malfunction_start_time', models.DateField()),
                ('malfunction_stop_time', models.DateField()),
                ('notify_persion', models.CharField(max_length=50)),
                ('record_persion', models.CharField(db_index=True, max_length=50)),
                ('malfunction_content', models.TextField()),
                ('event_status', models.BooleanField(db_index=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RecordPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malfunction_start_time', models.DateField()),
                ('malfunction_stop_time', models.DateField()),
                ('malfunction_type', models.IntegerField()),
                ('malfunction_responsibility', models.IntegerField()),
                ('notify_persion', models.CharField(max_length=50)),
                ('record_persion', models.CharField(db_index=True, max_length=50)),
                ('malfunction_content', models.TextField()),
                ('event_status', models.BooleanField(db_index=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
    ]
