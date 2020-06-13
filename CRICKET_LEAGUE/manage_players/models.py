from django.db import models
from manage_teams.models import Team

class Player(models.Model):
    identifier = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image_uri = models.ImageField(upload_to='media')
    jersey_number = models.CharField(max_length=3)
    country = models.CharField(max_length=50)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,blank=True,null=True)
    #Player history (matches, run, highest scores, fifties, hundreds)


