# Generated by Django 5.0.6 on 2024-08-07 03:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roster',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='sidepot',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
