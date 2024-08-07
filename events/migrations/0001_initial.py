# Generated by Django 5.0.6 on 2024-08-06 02:41

import django.contrib.postgres.fields
import django.core.validators
import django.db.models.deletion
import localflavor.us.models
import phonenumber_field.modelfields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BowlingCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('street_address', models.CharField(max_length=128, verbose_name='address')),
                ('city', models.CharField(max_length=64)),
                ('state', localflavor.us.models.USStateField(max_length=2)),
                ('zip_code', localflavor.us.models.USZipCodeField(max_length=10)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(blank=True, max_length=128, null=True)),
                ('website', models.URLField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=256)),
                ('is_archived', models.BooleanField(default=False)),
                ('admins', models.ManyToManyField(related_name='admined_events', to='profiles.profile')),
                ('bowling_centers', models.ManyToManyField(related_name='events', to='events.bowlingcenter')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_events', to='profiles.profile')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('date', models.DateField()),
                ('is_registration_open', models.BooleanField(default=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rosters', to='events.event')),
            ],
            options={
                'unique_together': {('event', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='RosterEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('handicap', models.PositiveIntegerField(blank=True, default=0)),
                ('bowler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roster_entries', to='profiles.profile')),
                ('roster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roster_entries', to='events.roster')),
            ],
        ),
        migrations.CreateModel(
            name='BowlerSidepotEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_count', models.PositiveIntegerField(default=0)),
                ('roster_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bowler_sidepot_entries', to='events.rosterentry')),
            ],
        ),
        migrations.CreateModel(
            name='Sidepot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('type', models.CharField(choices=[('HG', 'High Game'), ('HS', 'High Series'), ('WTA', 'Winner Takes All'), ('Elim', 'Eliminator'), ('MD', 'Mystery Doubles')], max_length=64)),
                ('entry_fee', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payout_ratio', models.PositiveSmallIntegerField(default=6, validators=[django.core.validators.MinValueValidator(2)])),
                ('is_handicap', models.BooleanField(default=False)),
                ('games_used', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, size=None)),
                ('is_reverse', models.BooleanField(blank=True, default=False)),
                ('allow_multiple_entries', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sidepots', to='events.event')),
            ],
            options={
                'unique_together': {('event', 'type', 'is_handicap', 'games_used', 'is_reverse')},
            },
        ),
        migrations.AddField(
            model_name='rosterentry',
            name='sidepots',
            field=models.ManyToManyField(through='events.BowlerSidepotEntry', to='events.sidepot'),
        ),
        migrations.AddField(
            model_name='bowlersidepotentry',
            name='sidepot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.sidepot'),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_number', models.PositiveIntegerField()),
                ('scr_score', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(300)])),
                ('bowler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_scores', to='events.rosterentry')),
            ],
            options={
                'unique_together': {('bowler', 'game_number')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='rosterentry',
            unique_together={('roster', 'bowler')},
        ),
    ]
