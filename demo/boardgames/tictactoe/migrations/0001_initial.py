# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=1, default='A', choices=[('A', 'Active'), ('F', 'First Player Wins'), ('S', 'Second Player Wins'), ('D', 'Draw')])),
                ('first_player', models.ForeignKey(related_name='games_first_player', to=settings.AUTH_USER_MODEL)),
                ('next_to_move', models.ForeignKey(related_name='games_to_move', to=settings.AUTH_USER_MODEL)),
                ('second_player', models.ForeignKey(related_name='games_second_player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('message', models.CharField(verbose_name='Optional Message', max_length=300, blank=True, help_text='Adding a friendly message is never a bad idea!')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(related_name='invitations_sent', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(verbose_name='User to invite', help_text='Please select the user you want to play a game with', related_name='invitations_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('x', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('y', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('comment', models.CharField(max_length=300)),
                ('by_first_player', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(to='tictactoe.Game')),
            ],
            options={
                'get_latest_by': 'timestamp',
            },
        ),
    ]
