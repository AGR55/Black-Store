# Generated by Django 4.2.7 on 2024-01-01 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderline',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderline',
            old_name='product_id',
            new_name='product',
        ),
    ]
