# Generated by Django 3.0.3 on 2020-09-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('unit', models.CharField(choices=[('Square feet', 'square feet'), ('Square meter', 'square meter'), ('Square Yard', 'Square Yard'), ('Marla', 'marla'), ('Kanal', 'kanal')], max_length=12)),
                ('bedrooms', models.PositiveIntegerField()),
                ('bathroom', models.PositiveIntegerField()),
                ('image_house', models.ImageField(upload_to='property')),
                ('purpose', models.CharField(choices=[('Sale', 'sale'), ('Rent', 'rent')], max_length=4)),
                ('type', models.CharField(choices=[('Plot', 'plot'), ('Commercial', 'commercial'), ('House', 'house')], max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('sector', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
