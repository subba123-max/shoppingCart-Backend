# Generated by Django 2.2.13 on 2021-01-05 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0004_orders_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders_items',
            name='price',
        ),
    ]
