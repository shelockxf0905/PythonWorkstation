# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtime', models.DateTimeField(auto_now=True, verbose_name='\u505a\u68a6\u65f6\u95f4', auto_created=True)),
                ('content', models.CharField(max_length=300)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-dtime'],
                'verbose_name': '\u68a6\u60f3\u6e05\u5355',
            },
        ),
    ]
