from django.db import models
from fixtures_points.models import Fixture 
from manage_teams.models import Team 


class Point(models.Model):
    identifier = models.AutoField(primary_key=True)
    winner = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='winner',blank=False,null=True)
    winner_point = models.IntegerField(default=3)
    loser_point = models.IntegerField(default=0)

    @classmethod
    def create(cls, team):
        point_obj = cls(winner=team)
        return point_obj


class Match(models.Model):
    identifier = models.AutoField(primary_key=True)
    fixture = models.OneToOneField(Fixture, on_delete=models.CASCADE,blank=True,null=True)
    point = models.OneToOneField(Point, on_delete=models.CASCADE,blank=True,null=True)

    @classmethod
    def create(cls, fixture,point):
        match_obj = cls(fixture=fixture,point=point)
        return match_obj



    

