# Generated by Django 3.0.3 on 2020-10-02 22:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0027_auto_20201003_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerproperty',
            name='size',
            field=models.CharField(max_length=1000000, validators=[django.core.validators.RegexValidator('(\\d{1000000})$', 'Value less than 1000000 are allowed')]),
        ),
    ]
