# Generated by Django 2.2.12 on 2022-12-31 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepdive', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
