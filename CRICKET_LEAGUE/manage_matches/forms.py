from django import forms
from .models import Match,Point

class MatchDetailForm(forms.ModelForm):
    class Meta():
        model = Match
        fields= '__all__'


class PoimtDetailForm(forms.ModelForm):
    class Meta():
        model = Point
        fields= '__all__'
