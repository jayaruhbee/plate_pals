# Generated by Django 4.2.4 on 2023-08-22 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_user_image_user_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image_url',
        ),
    ]