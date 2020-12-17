# Generated by Django 3.0.3 on 2020-10-02 22:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0024_auto_20201003_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerproperty',
            name='bathroom',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator('^[0-9]{999}$', 'Value less than 999 are allowed')]),
        ),
        migrations.AlterField(
            model_name='sellerproperty',
            name='bedrooms',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator('^[0-9]{999}$', 'Value less than 999 are allowed')]),
        ),
        migrations.AlterField(
            model_name='sellerproperty',
            name='size',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator('^[0-9]{1000000}$', 'Value less than 1000000 are allowed')]),
        ),
    ]
