# Generated by Django 3.2.13 on 2022-05-14 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_review_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='purchase_link',
            field=models.URLField(blank=True, max_length=400),
        ),
    ]
