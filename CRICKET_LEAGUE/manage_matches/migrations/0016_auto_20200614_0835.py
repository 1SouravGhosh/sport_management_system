# Generated by Django 3.0.7 on 2020-06-14 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_teams', '0001_initial'),
        ('manage_matches', '0015_remove_point_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='match_suspended',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='point',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='manage_teams.Team'),
        ),
    ]
