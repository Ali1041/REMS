# Generated by Django 3.0.3 on 2020-09-30 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0020_auto_20200929_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approve',
            name='approval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approval_seller', to='seller.SellerProperty'),
        ),
    ]
