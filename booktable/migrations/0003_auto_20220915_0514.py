# Generated by Django 3.2.15 on 2022-09-15 05:14

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktable', '0002_auto_20220913_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='featured_image',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='menu_item',
        ),
        migrations.AddField(
            model_name='menu',
            name='course_description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='menu',
            name='course_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='menu',
            name='course_name',
            field=models.CharField(default='', max_length=25, unique=True),
        ),
    ]