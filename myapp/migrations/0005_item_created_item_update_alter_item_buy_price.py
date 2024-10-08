# Generated by Django 5.0.7 on 2024-08-08 22:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_price_item_buy_price_item_sell_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='buy_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
