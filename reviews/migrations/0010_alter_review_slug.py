# Generated by Django 3.2.13 on 2022-05-10 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_alter_review_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]