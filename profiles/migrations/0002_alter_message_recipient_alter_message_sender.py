# Generated by Django 5.0.6 on 2024-08-25 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='received_messages',
                to='profiles.profile',
            ),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='sent_messages',
                to='profiles.profile',
            ),
        ),
    ]
