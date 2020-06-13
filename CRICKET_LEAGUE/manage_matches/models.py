from django.db import models


class Match(models.Model):
    identifier = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=True)
    team1 = models.CharField(max_length=255)
    team2 = models.CharField(max_length=255)
    winner = models.CharField(max_length=10)
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    #Player history (matches, run, highest scores, fifties, hundreds)



