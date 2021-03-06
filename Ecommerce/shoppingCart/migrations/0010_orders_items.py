# Generated by Django 2.2.13 on 2021-01-05 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoppingCart', '0009_delete_orders_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingCart.Orders')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingCart.Products')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
