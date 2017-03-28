# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('interactive', '0003_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='message',
            field=models.CharField(verbose_name='Optional Message', max_length=300, blank=True, help_text='Add a friendly message is always a good idea'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='to_user',
            field=models.ForeignKey(verbose_name='User to invite', help_text='Please select the user you want to play a game with', related_name='invitations_received', to=settings.AUTH_USER_MODEL),
        ),
    ]
