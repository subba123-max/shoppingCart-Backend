# Generated by Django 2.2.13 on 2021-01-05 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0011_remove_orders_items_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders_items',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]
