# Generated by Django 5.0.7 on 2024-09-17 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_sale_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='barcode',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
