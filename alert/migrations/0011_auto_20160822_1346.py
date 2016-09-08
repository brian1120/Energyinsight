# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0010_alertlog_alert_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertlog',
            name='description',
            field=tinymce.models.HTMLField(default=None, max_length=100000, null=True, blank=True),
        ),
    ]
