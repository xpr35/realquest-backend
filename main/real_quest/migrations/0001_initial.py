# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 11:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PartyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Empty', 'empty'), ('Not Full', 'not_full'), ('Full', 'full')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QuestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('tags', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='QuestStages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Waiting', 'waiting'), ('In Progress', 'in_progress'), ('Done', 'done')], max_length=255)),
                ('cost', models.FloatField()),
                ('proof', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_model', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='questmodel',
            name='consumer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consumer_model', to='real_quest.UserModel'),
        ),
        migrations.AddField(
            model_name='questmodel',
            name='producer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='producer_model', to='real_quest.UserModel'),
        ),
        migrations.AddField(
            model_name='questmodel',
            name='stages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_quest.QuestStages'),
        ),
        migrations.AddField(
            model_name='partymodel',
            name='leader',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leader_model', to='real_quest.UserModel'),
        ),
        migrations.AddField(
            model_name='partymodel',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_quest.UserModel'),
        ),
    ]
