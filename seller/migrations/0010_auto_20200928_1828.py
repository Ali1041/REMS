# Generated by Django 3.0.3 on 2020-09-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0009_auto_20200927_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerproperty',
            name='type',
            field=models.CharField(choices=[{'plot', 'Plot'}, {'commercial', 'Commercial'}, {'House', 'house'}], max_length=10),
        ),
    ]