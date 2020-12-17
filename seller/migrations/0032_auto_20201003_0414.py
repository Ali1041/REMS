# Generated by Django 3.0.3 on 2020-10-02 23:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0031_auto_20201003_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerproperty',
            name='city',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$', 'Only alphabetic characters are allowed.')]),
        ),
    ]
