from django.db import models
# from manage_matches.models import Match
from manage_teams.models import Team


class Group(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name


class Fixture(models.Model):
    identifier = models.AutoField(primary_key=True)
    team1 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team1',blank=False,null=True)
    team2 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team2',blank=False,null=True)
    date = models.DateField(auto_now=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='fixtures',blank=False,null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return "Fixture no. " + str(self.identifier) + " of " + self.group.name

    





