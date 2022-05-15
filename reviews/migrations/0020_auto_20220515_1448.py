# Generated by Django 3.2.13 on 2022-05-15 14:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0019_alter_review_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='slug',
        ),
        migrations.AlterField(
            model_name='review',
            name='book_cover',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dpsodnurd/image/upload/v1652618629/zhtctppqjky78q8h760n.jpg', max_length=255, verbose_name='image'),
        ),
    ]
