# Generated by Django 3.0.3 on 2020-09-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_sellerproperty_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approve',
            name='request_approval',
            field=models.CharField(choices=[('Approve', 'Approve'), ('Reject', 'Reject'), ('Sold', 'Sold')], max_length=10),
        ),
    ]