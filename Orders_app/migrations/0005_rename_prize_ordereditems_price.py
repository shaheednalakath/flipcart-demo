# Generated by Django 5.1.3 on 2025-01-04 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders_app', '0004_alter_ordereditems_prize_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordereditems',
            old_name='prize',
            new_name='price',
        ),
    ]
