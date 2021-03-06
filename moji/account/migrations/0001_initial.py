# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-11 16:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=40, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_of_birth', models.DateField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brief', models.TextField()),
                ('violation', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='AccountRequest',
            fields=[
                ('accept', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('userFrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL)),
                ('userTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LastSeen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_of_seen', models.GenericIPAddressField(editable=False)),
                ('time_and_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('age', models.DateTimeField(blank=True, null=True)),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('link1', models.URLField(blank=True, null=True)),
                ('link2', models.URLField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=150, null=True)),
                ('strikes', models.IntegerField(blank=True, default=0)),
                ('suspended', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=True)),
                ('celeb', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content_requires_18', models.BooleanField(default=False)),
                ('blocked', models.ManyToManyField(blank=True, related_name='blocked_by', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, related_name='followed_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
