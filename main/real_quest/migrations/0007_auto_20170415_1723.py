# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('real_quest', '0006_auto_20170415_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queststages',
            name='quest',
        ),
        migrations.AddField(
            model_name='questmodel',
            name='stages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='real_quest.QuestStages'),
        ),
    ]
