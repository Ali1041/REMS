# Generated by Django 3.0.3 on 2020-09-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0010_auto_20200928_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerproperty',
            name='type',
            field=models.CharField(choices=[('Plot', 'plot'), ('Commercial', 'commercial'), ('House', 'house')], max_length=10),
        ),
    ]
