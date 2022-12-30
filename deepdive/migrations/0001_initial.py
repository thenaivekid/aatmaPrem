# Generated by Django 2.2.12 on 2022-12-30 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('desc', models.CharField(max_length=1024)),
                ('page', models.CharField(max_length=16)),
                ('item', models.ManyToManyField(blank=True, related_name='item', to='deepdive.PostItem')),
            ],
        ),
        migrations.CreateModel(
            name='AnalyzingPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=32)),
                ('openness', models.IntegerField(default=0)),
                ('conscientiousness', models.IntegerField(default=0)),
                ('extroversion', models.IntegerField(default=0)),
                ('agreeableness', models.IntegerField(default=0)),
                ('neuroticism', models.IntegerField(default=0)),
                ('values', models.CharField(max_length=256)),
                ('passions', models.CharField(max_length=256)),
                ('similarities', models.CharField(max_length=256)),
                ('importance', models.CharField(max_length=256)),
                ('darkside', models.CharField(max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]