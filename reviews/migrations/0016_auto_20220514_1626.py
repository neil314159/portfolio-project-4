# Generated by Django 3.2.13 on 2022-05-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0015_alter_review_purchase_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='star_rating2',
        ),
        migrations.AlterField(
            model_name='review',
            name='star_rating',
            field=models.IntegerField(choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')], default=5),
        ),
    ]
