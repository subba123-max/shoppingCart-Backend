# Generated by Django 2.2.13 on 2021-01-05 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoppingCart', '0007_remove_orders_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders_items',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
