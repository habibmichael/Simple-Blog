# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 5, 19, 55, 42, 868469, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
