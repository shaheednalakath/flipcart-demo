# Generated by Django 5.1.3 on 2024-12-27 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer_app', '0001_initial'),
        ('Products_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.IntegerField(choices=[(2, 'ORDER_PROCESSED'), (3, 'ORDER_DELIVERED'), (4, 'ORDER_REJECTED')], default=0)),
                ('delete_status', models.IntegerField(choices=[(1, 'Live'), (0, 'Delete')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='Customer_app.customers')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.ImageField(default=1, upload_to='')),
                ('size', models.IntegerField()),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cartitems', to='Products_app.products')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_items', to='Orders_app.orders')),
            ],
        ),
    ]
