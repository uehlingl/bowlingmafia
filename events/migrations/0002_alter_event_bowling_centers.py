# Generated by Django 5.0.6 on 2024-07-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='bowling_centers',
            field=models.ManyToManyField(related_name='events', to='events.bowlingcenter'),
        ),
    ]
