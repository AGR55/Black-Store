# Generated by Django 4.2.7 on 2023-12-24 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
