# Generated by Django 4.2.7 on 2023-12-26 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_alter_service_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
    ]
