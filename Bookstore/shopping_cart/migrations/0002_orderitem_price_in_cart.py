# Generated by Django 3.0.3 on 2020-03-30 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price_in_cart',
            field=models.FloatField(default='0.00'),
        ),
    ]