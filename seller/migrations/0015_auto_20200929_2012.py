# Generated by Django 3.0.3 on 2020-09-29 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0014_auto_20200929_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerproperty',
            name='timestamp',
            field=models.DateTimeField(default=datetime.timezone),
        ),
    ]