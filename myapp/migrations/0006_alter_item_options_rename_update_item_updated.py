# Generated by Django 5.0.7 on 2024-08-08 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_item_created_item_update_alter_item_buy_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='update',
            new_name='updated',
        ),
    ]
