# Generated by Django 3.2.13 on 2022-05-08 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='purchase_link',
            field=models.CharField(max_length=300),
        ),
    ]
