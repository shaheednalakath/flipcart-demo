# Generated by Django 5.1.3 on 2025-01-04 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders_app', '0003_ordereditems_prize_orders_total_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditems',
            name='prize',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total_product_price',
            field=models.IntegerField(default=0),
        ),
    ]
