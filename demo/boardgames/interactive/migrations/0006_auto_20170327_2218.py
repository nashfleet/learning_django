# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interactive', '0005_auto_20170327_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='message',
            field=models.CharField(verbose_name='Optional Message', max_length=300, blank=True, null=True, help_text='Add a friendly message is always a good idea'),
        ),
    ]
