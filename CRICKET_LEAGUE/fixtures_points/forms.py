from django import forms
from .models import Fixture,Group


class FixtureDetailForm(forms.ModelForm):
    class Meta():
        model = Fixture
        fields=['team1','team2','date','group','completed']

class GroupDetailForm(forms.ModelForm):
    class Meta():
        model = Group
        fields=['name']
