# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_app.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fileName', models.ImageField(upload_to=image_app.models.get_datetime)),
                ('Duplicate', models.BooleanField(default=False)),
                ('Hash', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
