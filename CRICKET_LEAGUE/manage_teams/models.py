from django.db import models


class Team(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo_uri = models.ImageField(upload_to='media')
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.name
