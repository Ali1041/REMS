# Generated by Django 3.0.3 on 2020-10-02 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0022_auto_20201003_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerproperty',
            name='bedrooms',
            field=models.PositiveIntegerField(),
        ),
    ]
