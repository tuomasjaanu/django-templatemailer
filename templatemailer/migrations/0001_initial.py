# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-28 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('subject', models.CharField(max_length=255)),
                ('plain_text', models.TextField()),
                ('html', models.TextField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to=b'email_template_attachments')),
                ('language_code', models.CharField(default=b'en', max_length=16)),
            ],
        ),
    ]
