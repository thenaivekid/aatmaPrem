# Generated by Django 2.2.12 on 2022-12-31 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepdive', '0005_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]