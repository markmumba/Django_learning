# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-28 06:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsletterrecipients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]