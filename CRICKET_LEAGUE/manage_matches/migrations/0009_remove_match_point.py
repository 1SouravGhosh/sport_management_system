# Generated by Django 3.0.7 on 2020-06-14 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_matches', '0008_remove_point_match_suspended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='point',
        ),
    ]
