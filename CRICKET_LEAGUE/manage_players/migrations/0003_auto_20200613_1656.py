# Generated by Django 3.0.7 on 2020-06-13 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_players', '0002_auto_20200613_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image_uri',
            field=models.ImageField(upload_to='manage_players/images/profile_images'),
        ),
    ]
