# Generated by Django 3.0.3 on 2020-09-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0015_auto_20200929_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerproperty',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
