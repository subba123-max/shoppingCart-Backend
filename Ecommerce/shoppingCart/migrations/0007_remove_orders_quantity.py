# Generated by Django 2.2.13 on 2021-01-05 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0006_orders_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='Quantity',
        ),
    ]
